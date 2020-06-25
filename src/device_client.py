from event_producer import EventProducer
from random import randrange
publisher = EventProducer()
publisher.connect()
publisher.publish_event("list/command", "get_item|{}".format(randrange(10)))


