from kafka import KafkaConsumer

import json

topic_name = 'pending'
consumer = KafkaConsumer(
    topic_name,
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='my-group',
    value_deserializer=lambda x: json.loads(x.decode('utf8'))
)


for message in consumer:
    message = message.value
    print(message)
    print(type(message))
