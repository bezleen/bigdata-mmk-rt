import findspark
findspark.init()
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
from kafka import KafkaProducer
import json
import random
TOPIC_FINDING = 'finding'
TOPIC_PENDING = 'pending'
sc = SparkContext("local[2]", "KafkaStreamingExample")
batchInterval=5
ssc = StreamingContext(sc, batchInterval)
kafka_server = "localhost:9092"
kafkaParams = {"metadata.broker.list": kafka_server, "auto.offset.reset": "smallest"}
kafkaStream = KafkaUtils.createDirectStream(ssc, ["pending"], kafkaParams)


def predict(data):
    # TODO: format value
    data = []
    user_id = data['user_id']
    tier = random.choice([1,2,3,4,5,6,7,8,9])
    # TODO: predict the tier
    return {
        "user_id": user_id,
        "tier": str(tier)
    }

def process_partition(iter):
    kafka_producer = KafkaProducer(bootstrap_servers=kafka_server, value_serializer=lambda x: json.dumps(x).encode('utf-8'))
    for record in iter:
        value = record[1]
        print(value)
        predicted = predict(value)
        kafka_producer.send(TOPIC_PENDING, value=predicted)

kafkaStream.foreachRDD(lambda rdd: rdd.foreachPartition(process_partition))


ssc.start()
ssc.awaitTermination()


