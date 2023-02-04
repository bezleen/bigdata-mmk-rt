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
        self.dict_findings = {}
        """
        self.dict_findings = {
            "<user_id>": 1,
        }
        """

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
        Controller.MMK.find_match(user_id)
        # emit
        socketio.emit("finding", {"user_id": user_id, "status": "finding", "req_id": sid}, namespace=self.namespace, to=user_id)
        return
