from flask_socketio import Namespace
from flask_socketio import join_room, leave_room, rooms
from flask import request
import pydash as py_


class MMK(Namespace):
    def __init__(self, namespace=None):
        self.namespace = namespace
        super().__init__(namespace)

    def on_connect(self, *args, **kwargs):
        sid = request.sid
        return
    
    def on_find(self, *args, **kwargs):
        sid = request.sid