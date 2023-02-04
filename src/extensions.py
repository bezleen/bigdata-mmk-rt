import json

from flask_socketio import SocketIO
from flask_pymongo import PyMongo
from kafka import KafkaConsumer, KafkaProducer

import src.constants as Consts

socketio = SocketIO(cors_allowed_origins="*")
mdb = PyMongo()
kafka_producer = KafkaProducer(bootstrap_servers=Consts.KAFKA_SERVER, value_serializer=lambda x: json.dumps(x).encode('utf-8'))
