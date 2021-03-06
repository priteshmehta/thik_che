import paho.mqtt.client as mqtt
from config import BROKER_IP, BROKER_PORT
from cache_manager import CacheManager

class EventProducer:
	def __init__(self):
		self.mqtt_client = mqtt.Client(client_id='publisher-1')
		self.mqtt_client.on_connect = self.connect_msg
		self.mqtt_client.on_publish = self.publish_msg

	def connect_msg(self):
		print('Connected to Broker')


	def publish_msg(self):
		print('Message Published')

	def connect(self):
		self.mqtt_client.connect(BROKER_IP, BROKER_PORT, 60)

	def publish_event(self, topic, event):
		# Publish a message with topic
		print("Msg published")
		ret = self.mqtt_client.publish(topic, event)
		print("Return:", ret)
		# Run a loop
		#self.mqtt_client.loop()

	def disconnect(self):
		self.mqtt_client.disconnect()
