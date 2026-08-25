import json
from kafka import KafkaConsumer

consumer=KafkaConsumer(
    "dbserver.public.customers",
    bootstrap_servers="localhost:9092",
    auto_offset_reset="earliest",
    value_deserializer=lambda x: json.loads(x.decode()) if x else None
)
for msg in consumer:
    print("CDC EVENT:", msg.value)
