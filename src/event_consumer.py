import paho.mqtt.client as mqtt
from config import BROKER_IP, BROKER_PORT
from cache_manager import CacheManager

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

	def process_message(self, client, userdata, message):
		"""Process received messages
		"""
		msg_payload = str(message.payload.decode("utf-8"))
		print("message received: {}".format(msg_payload))
		self.cache.set("mylist", msg_payload)
		#print("message topic=", message.topic)
		#print("message qos=", message.qos)
		#print("message retain flag=", message.retain)

	def subscribe_mylist(self):
		"""Connect to broker
		"""
		self.mqtt_client.subscribe("house/light")

	def run_loop(self):
		"""Run loop
		"""
		self.mqtt_client.loop_forever()

print("MQTT Event Consumer is running...")
event_consumer = EventConsumer()
event_consumer.connect()
event_consumer.mqtt_client.loop_forever()
