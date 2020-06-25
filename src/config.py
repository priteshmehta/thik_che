# MQTT Broker

#BROKER_IP = "3.22.118.222"
BROKER_IP = "127.0.0.1"
BROKER_PORT = 1883

# Redis cache
REDIS_HOST = "localhost"
REDIS_PORT = 6379
REDIS_PASSWORD = ""


#mosquitto_pub -h 127.0.0.1 -p 1883 -t list/command -m "get_item|1"
#mosquitto_sub -h 127.0.0.1 -p 1883 -t list/command