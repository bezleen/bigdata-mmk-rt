import findspark
findspark.init()
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
from kafka import KafkaProducer
import json
import random
import pickle
TOPIC_FINDING = 'finding'
TOPIC_PENDING = 'pending'
sc = SparkContext("local[2]", "KafkaStreamingExample")
batchInterval = 5
ssc = StreamingContext(sc, batchInterval)
kafka_server = "localhost:9092"
kafkaParams = {"metadata.broker.list": kafka_server, "auto.offset.reset": "smallest"}
kafkaStream = KafkaUtils.createDirectStream(ssc, [TOPIC_FINDING], kafkaParams)


def predict(model, data):
    # TODO: format value
    data = json.loads(data)
    user_id = data.get('user_id')
    kd = float(data.get("kd"))
    kill = float(data.get("kill"))
    death = float(data.get("death"))
    assistant = float(data.get("assistant"))
    win_rate = float(data.get("win_rate"))
    pick_rate = float(data.get("pick_rate"))
    avg_score = float(data.get("avg_score"))
    first_blood_rate = float(data.get("first_blood_rate"))
    headshot_rate = float(data.get("headshot_rate"))
    # TODO: predict the tier
    tiers = model.predict([[kd, kill, death, assistant, win_rate, pick_rate, avg_score, first_blood_rate, headshot_rate]])
    tier = tiers[0]
    # tier = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9])
    return {
        "user_id": user_id,
        "tier": str(tier)
    }


def process_partition(iter):
    kafka_producer = KafkaProducer(bootstrap_servers=kafka_server, value_serializer=lambda x: json.dumps(x).encode('utf-8'))
    model = pickle.load(open("spark_streaming/ml_models/rf_valorent.model", 'rb'))
    for record in iter:
        value = record[1]
        print(value)
        predicted = predict(model, value)
        print(predicted)
        kafka_producer.send(TOPIC_PENDING, value=predicted)


kafkaStream.foreachRDD(lambda rdd: rdd.foreachPartition(process_partition))


ssc.start()
ssc.awaitTermination()
