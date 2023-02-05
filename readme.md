# 1. run kafka
## change directory
cd kafka
## run kafka
docker-compose up -d --build
## ssh container kafka
docker exec -it broker sh

## create topic kafka
kafka-topics --bootstrap-server broker:9092 --topic finding --create --partitions 3 --replication-factor 1
kafka-topics --bootstrap-server broker:9092 --topic pending --create --partitions 3 --replication-factor 1

# 2. run server socket-io
cd ..
docker-compose up -d --build

# 3. run model server
