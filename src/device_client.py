from event_producer import EventProducer

publisher = EventProducer()
publisher.connect()
publisher.publish_event("list/command", "get_item|1")


