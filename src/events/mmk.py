from flask_socketio import Namespace
from flask_socketio import join_room, leave_room, rooms
from flask import request
import pydash as py_
import src.controllers as Controller
from src.extensions import socketio


class MMK(Namespace):
    def __init__(self, namespace=None):
        self.namespace = namespace
        super().__init__(namespace)
        self.mmk_class = Controller.MMK(namespace=self.namespace)

    def on_connect(self, *args, **kwargs):
        sid = request.sid
        return

    def on_find(self, *args, **kwargs):
        sid = request.sid
        args = args[0]
        user_id = py_.get(args, "user_id")
        # join room
        rooms_joined = rooms(sid=sid, namespace=self.namespace)
        if user_id not in rooms_joined:
            join_room(user_id, sid=sid, namespace=self.namespace)
        # find match
        self.mmk_class.find_match(user_id, sid)
        return

    def on_test(self, *args, **kwargs):
        sid = request.sid
        args = args[0]
        user_id = py_.get(args, "user_id")
        self.mmk_class.get_test(user_id)
        return
