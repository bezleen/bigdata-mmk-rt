
from flask_socketio import SocketIO
from flask_pymongo import PyMongo
from kafka import KafkaConsumer, KafkaProducer


socketio = SocketIO(cors_allowed_origins="*")
mdb = PyMongo()

