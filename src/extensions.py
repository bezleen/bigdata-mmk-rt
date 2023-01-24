
from flask_socketio import SocketIO
from flask_pymongo import PyMongo

socketio = SocketIO(cors_allowed_origins="*")
mdb = PyMongo()