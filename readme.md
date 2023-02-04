# create topic kafka
kafka-topics --bootstrap-server broker:9092 --topic finding --create --partitions 3 --replication-factor 1
kafka-topics --bootstrap-server broker:9092 --topic pending --create --partitions 3 --replication-factor 1

# kafka
https://23a5-171-252-189-91.ap.ngrok.io