# create topic kafka
kafka-topics --bootstrap-server broker:9092 --topic finding --create --partitions 3 --replication-factor 1
kafka-topics --bootstrap-server broker:9092 --topic pending --create --partitions 3 --replication-factor 1
