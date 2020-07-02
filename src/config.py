# MQTT Broker

#BROKER_IP = "3.22.118.222"
BROKER_IP = "127.0.0.1"
BROKER_PORT = 1883

# Redis cache
REDIS_HOST = "localhost"
REDIS_PORT = 6379
REDIS_PASSWORD = ""
device_id = "db19ab8503f34505a17e081f155a9714"


#mosquitto_pub -h 127.0.0.1 -p 1883 -t list/command -m "get_item|1"
#mosquitto_sub -h 127.0.0.1 -p 1883 -t list/command/res
#mosquitto_sub -h 3.22.118.222 -p 1883 -t list/command/res
#mosquitto_pub -h 3.22.118.222 -p 1883 -t list/command -m "add_item|0001"
#mosquitto_sub -h 127.0.0.1 -p 1883 -d -t '$SYS/broker/clients/connected' - Total number of connection
#mosquitto_sub -h 3.22.118.222 -p 1883 -d -t '$SYS/broker/messages/received' Msg received
#mosquitto_sub -h 3.22.118.222 -p 1883 -d -t  '$SYS/broker/messages/sent'
#mosquitto_sub -h 3.22.118.222 -p 1883 -d -t '$SYS/broker/messages/count'
#https://www.hivemq.com/blog/mqtt-essentials-part-5-mqtt-topics-best-practices/
