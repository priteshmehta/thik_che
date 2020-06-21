import paho.mqtt.client as mqtt
from config import BROKER_IP, BROKER_PORT
from cache_manager import CacheManager
from db_manager import master_list
from event_producer import EventProducer


class EventConsumer:
	def __init__(self):
		self.mqtt_client = mqtt.Client(client_id="sub1")
		self.mqtt_client.on_message = self.process_message
		self.cache = CacheManager()

	def connect(self):
		"""Connect to broker
		"""
		self.mqtt_client.connect(BROKER_IP, BROKER_PORT, 60)
		self.mqtt_client.subscribe("list/mylist")
		self.mqtt_client.subscribe("list/command")

	def process_message(self, client, userdata, message):
		"""Process received messages
		"""
		msg_payload = str(message.payload.decode("utf-8"))
		print("topic: {}, message received: {}".format(message.topic, msg_payload))
		if message.topic == "list/mylist":
			self.cache.set("mylist", msg_payload)
		elif message.topic == "list/command":
			cmd, arg = msg_payload.split("|")
			print("command: {} arg: {}".format(cmd, arg))
			self.process_command(cmd, arg)
		else:
			print("invalid topic")

		#print("message topic=", message.topic)
		#print("message qos=", message.qos)
		#print("message retain flag=", message.retain)

	def process_command(slef, cmd, arg):
		if cmd == "get_item":
			try:
				item = master_list[int(arg)]
				print(item)
				item_str = "{}|{}".format(item["id"], item["name"])
				print(item_str)
				publisher = EventProducer()
				publisher.connect()
				publisher.publish_event("list/mylist", item_str)
			except Exception as e:
				#print("invalid item. Available items are", master_list)
				print(e)

		else:
			print("Invalid command")


	def run_loop(self):
		"""Run loop
		"""
		self.mqtt_client.loop_forever()

print("MQTT Event Consumer is running...")
event_consumer = EventConsumer()
event_consumer.connect()
event_consumer.mqtt_client.loop_forever()
