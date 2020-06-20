import random
import string
from random import randint

from event_producer import EventProducer
from cache_manager import CacheManager

if __name__ == "__main__":
	publisher = EventProducer()
	publisher.connect()
	#Pushing random items
	item_name = "item" + str(randint(0, 9999999999))
	publisher.publish_event(item_name)

	print("Data in cache")
	cache = CacheManager()
	cache.print_data("mylist")