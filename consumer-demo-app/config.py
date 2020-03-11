
import os

defaults = {
    "BROKER": "pkc-e8mp5.eu-west-1.aws.confluent.cloud:9092",
    "GROUP_ID": "default-demo-consumer-id",
    "CONSUMER_TOPICS": ["spanda.poc.test.in"]
}


def resolve_config(key: str) -> str:
    maybe_value = os.environ.get(key)
    value = maybe_value and maybe_value.split() or None
    return value or defaults.get(key)
