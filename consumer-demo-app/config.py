
import os

defaults = {
    "BROKER": "localhost",
    "GROUP_ID": "default-demo-consumer-id",
    "CONSUMER_TOPICS": ["test_topic_in"],
    "PRODUCER_TOPICS": ["test_topic_out"]
}


def resolve_config(key: str) -> str:
    maybe_value = os.environ.get(key)
    value = maybe_value and maybe_value.split() or None
    return value or defaults.get(key)
