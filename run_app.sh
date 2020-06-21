#!/bin/bash
sudo systemctl restart mosquitto
sudo systemctl restart redis.service
python3 src/event_consumer.py