import json

from flask_socketio import SocketIO
from flask_pymongo import PyMongo


import src.constants as Consts

socketio = SocketIO(cors_allowed_origins="*")
mdb = PyMongo(directConnection=True)
