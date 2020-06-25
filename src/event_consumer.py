import time

import paho.mqtt.client as mqtt
from config import BROKER_IP, BROKER_PORT
from cache_manager import CacheManager
from db_manager import master_list
from event_producer import EventProducer

def process_message(client, userdata, message):
	"""Process received messages
	"""
	try:
		msg_payload = str(message.payload.decode("utf-8"))
		print("topic: {}, message received: {}".format(message.topic, msg_payload))
		cmd, arg = msg_payload.split("|")
		print("command: {} arg: {}".format(cmd, arg))
		cache_log = "timestamp: {}, Command: {}, arg:{}".format(cmd, arg, time.time())
		print("Cache: {}".format(cache_log))
		cache_client = CacheManager()
		cache_client.push("commands", cache_log)
		send_response(cmd, arg)
	except Exception as e:
		print("Error in processing message:{}".format(message.payload))
		print("Error:", e)

def on_connect(client, userdata, flags, rc):
	print("Connected with result code " + str(rc))
	client.subscribe("list/command")

def send_response(cmd, arg):
	"""Send response
	"""
	if cmd == "get_item":
		try:
			item = master_list[int(arg)]
			print(item)
			item_str = "{}|{}".format(item["id"], item["name"])
			print(item_str)
			publisher = EventProducer()
			publisher.connect()
			publisher.publish_event("list/command/res", item_str)
			publisher.disconnect()
		except Exception as e:
			#print("invalid item. Available items are", master_list)
			print(e)
	else:
		print("Invalid command")

if __name__ == "__main__":
	print("MQTT Event Consumer is running...")
	mqtt_client = mqtt.Client()
	mqtt_client.connect(BROKER_IP, BROKER_PORT, 60)
	mqtt_client.on_connect = on_connect
	mqtt_client.on_message = process_message
	mqtt_client.loop_forever()

