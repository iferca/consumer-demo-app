import logging
import sys
import config
from confluent_kafka.cimpl import Consumer, KafkaException

conf = {"bootstrap.servers": config.resolve_config("BROKER"),
        "group.id": config.resolve_config("GROUP_ID"),
        "session.timeout.ms": 6000,
        "auto.offset.reset": "earliest"}


def run_consumer():
    logger = logging.getLogger('consumer')
    logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter('%(asctime)-15s %(levelname)-8s %(message)s'))
    logger.addHandler(handler)

    consumer = Consumer(conf)
    consumer.subscribe(topics=config.resolve_config("CONSUMER_TOPICS"))

    try:
        while True:
            msg = consumer.poll(timeout=1.0)
            if msg is None:
                continue
            if msg.error():
                raise KafkaException(msg.error())
            else:
                # Proper message
                sys.stderr.write('%% %s [%d] at offset %d with key %s:\n' %
                                 (msg.topic(), msg.partition(), msg.offset(),
                                  str(msg.key())))
                print(msg.value())

    except KeyboardInterrupt:
        sys.stderr.write('%% Aborted by user\n')

    finally:
        # Close down consumer to commit final offsets.
        consumer.close()

