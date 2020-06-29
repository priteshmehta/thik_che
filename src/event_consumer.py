import time
import logging
import datetime

import paho.mqtt.client as mqtt
from config import BROKER_IP, BROKER_PORT
from cache_manager import CacheManager
from db_manager import master_list
from event_producer import EventProducer

class eventLogger:
	def __init__(self, log_file_name):
		formatter = logging.Formatter('%(asctime)s -  %(levelname)s - %(message)s')
		logging.basicConfig(level=logging.INFO)
		handler = logging.FileHandler(log_file_name)
		handler.setFormatter(formatter)
		self.logger = logging.getLogger(__name__)
		self.logger.addHandler(handler)

	def prefix(self, msg):
		"""Log info message with injected timestamp.
		"""
		now = datetime.datetime.now()
		time = now.strftime("%H:%M:%S.")
		time_milliseconds = time + "{0:03.0f}".format(now.microsecond / 1000)
		return u"{}: {}".format(time_milliseconds, msg)

	def info(self, msg, *args, **kwargs):
		self.logger.info(self.prefix(msg), *args, **kwargs)

	def warn(self, msg, *args, **kwargs):
		self.logger.warn(self.prefix(msg), *args, **kwargs)

	def error(self, msg, *args, **kwargs):
		self.logger.error(self.prefix(msg), *args, **kwargs)
	def debug(self, msg, *args, **kwargs):
		self.logger.debug(self.prefix(msg), *args, **kwargs)

eventLogger = eventLogger('event_consumer_log.log')
cache_client = CacheManager()

def add_item_mylist(item):
		"""add item to mylist
		"""
		shopping_list = "mylist"
		print("Add item to the list:", item)
		eventLogger.info("Adding item: {} to the:{}".format(item, shopping_list))
		cache_client.push(shopping_list, str(item))

def process_message(client, userdata, message):
	"""Process received messages
	"""
	try:
		msg_payload = str(message.payload.decode("utf-8"))
		print("topic: {}, message received: {}".format(message.topic, msg_payload))
		eventLogger.info("topic: {}, message received: {}".format(message.topic, msg_payload))
		cmd, arg = msg_payload.split("|")
		print("command: {} arg: {}".format(cmd, arg))
		if cmd == "get_item":
			send_response(cmd, arg)
		elif cmd == "add_item":
			for item in master_list:
				if arg == item["id"]:
					add_item_mylist((item["id"], item["name"]))
	except Exception as e:
		eventLogger.info("Error in processing message:{}".format(message.payload))
		eventLogger.error(e)

def on_connect(client, userdata, flags, rc):
	print("Connected with result code " + str(rc))
	client.subscribe("list/command")

def send_response(cmd, arg):
	"""Send response
	"""
	topic_name = "list/command/res"
	if cmd == "get_item":
		try:
			item = master_list[int(arg)]
			print(item)
			item_str = "{}|{}".format(item["id"], item["name"])
			eventLogger.info("topic: {}, publish: {}".format(topic_name, item_str))
			publisher = EventProducer()
			publisher.connect()
			publisher.publish_event(topic_name, item_str)
			publisher.disconnect()
		except Exception as e:
			#print("invalid item. Available items are", master_list)
			#print(e)
			eventLogger.info("Invalid item. Available items are : {}".format(master_list))
			eventLogger.error(e)
	else:
		print("Invalid command")


if __name__ == "__main__":
	print("MQTT Event Consumer is running...")
	mqtt_client = mqtt.Client()
	mqtt_client.connect(BROKER_IP, BROKER_PORT, 60)
	mqtt_client.on_connect = on_connect
	mqtt_client.on_message = process_message
	mqtt_client.loop_forever()

