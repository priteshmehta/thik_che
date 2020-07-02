import redis
from config import REDIS_HOST, REDIS_PORT, REDIS_PASSWORD

class CacheManager:
    def __init__(self):
        # The decode_repsonses flag here directs the client to convert the responses from Redis into Python strings
        # using the default encoding utf-8.  This is client specific.
        self.r = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD, decode_responses=True)

    def push(self, key, value):
        try:
            self.r.lpush(key, value)
        except Exception as e:
            print(e)

    def pop(self, key):
        try:
            self.r.pop(key)
        except Exception as e:
            print(e)

    def print_data(self, key):
        for i in range(0, self.r.llen(key)):
            print(self.r.lindex(key, i))

    def get_list_items(self, key):
        return [self.r.lindex(key, i) for i in range(0, self.r.llen(key))]

    def get_keys(self, pattern):
        return self.r.keys(pattern)

    def get_value(self, key):
        return self.r.get(key)

    def set_value(self, key, value):
        return self.r.set(key, value)

    def delete_key(self, key):
        return self.r.delete(key)
