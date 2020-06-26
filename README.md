
## Description

## Prerequisites

- Mosquitto
- Redis
- Python3

## Useful Commands

```
sudo systemctl restart mosquitto
sudo systemctl restart redis.service
```

### Test pub/sub
```
To Publish
mosquitto_pub -h 127.0.0.1 -p 1883 -t {TOPIC} -m {MSG}

To Subscribe
mosquitto_sub -h 127.0.0.1 -p 1883 -t {TOPIC}
```


### Redis cli
```
redis-cli ping
redic-cli --scan
redis-cli lindex {KEY_NAME} 0
redis-cli lpush {KEY_NAME} {VALUE}
redis-cli lpop {KEY_NAME}
```


### Run event consumer 
```
python3 src/event_consumer.py 
```

### tmux cli
```
tmux ls
tmux attach-session -t 0
Ctrl+b d
```




