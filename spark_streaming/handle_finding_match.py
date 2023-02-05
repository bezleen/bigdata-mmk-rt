import findspark
findspark.init()
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils

sc = SparkContext("local[2]", "KafkaStreamingExample")
batchInterval=5
ssc = StreamingContext(sc, batchInterval)

kafkaParams = {"metadata.broker.list": "localhost:9092", "auto.offset.reset": "smallest"}
topic = {"topic-name": 1}
kafkaStream = KafkaUtils.createDirectStream(ssc, ["pending"], kafkaParams)
# def process_partition(*args, **kwargs):
#     print("ok")
#     print(*args, **kwargs)
#     for value in args:
#         print(value)
#     return

def process_partition(iter):
    print("ok")
    for record in iter:
        key = record[0]
        value = record[1]
        print("Key: %s, Value: %s" % (key, value))

kafkaStream.foreachRDD(lambda rdd: rdd.foreachPartition(process_partition))



ssc.start()
ssc.awaitTermination()

