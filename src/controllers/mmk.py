
import pydash as py_


import src.functions as Funcs
import src.models.repo as Repo
from bson.objectid import ObjectId
from src.extensions import kafka_producer
import src.constants as Consts
from flask_socketio import emit, join_room, disconnect
from src.extensions import socketio


class MMK(object):

    @classmethod
    def find_match(cls, user_id):
        # get user data from database
        player_rate_data = Repo.mPlayerRate.get_item_with({"user_id": user_id})
        # print(player_rate_data)
        # print(type(player_rate_data))
        # user_id = row[0]
        kd = float(py_.get(player_rate_data, "kd"))
        kill = float(py_.get(player_rate_data, "kill"))
        death = float(py_.get(player_rate_data, "death"))
        assistant = float(py_.get(player_rate_data, "assistant"))
        win_rate = float(py_.get(player_rate_data, "win_rate"))
        pick_rate = float(py_.get(player_rate_data, "pick_rate"))
        avg_score = float(py_.get(player_rate_data, "avg_score"))
        first_blood_rate = float(py_.get(player_rate_data, "first_blood_rate"))
        headshot_rate = float(py_.get(player_rate_data, "headshot_rate"))
        record = {
            "user_id": user_id,
            "kd": kd,
            "kill": kill,
            "death": death,
            "assistant": assistant,
            "win_rate": win_rate,
            "pick_rate": pick_rate,
            "avg_score": avg_score,
            "first_blood_rate": first_blood_rate,
            "headshot_rate": headshot_rate
        }
        print(record)
        kafka_producer.send(Consts.TOPIC_FIND, value=record)
        # emit
        socketio.emit("start_finding", current_action.get_action(), namespace=self.namespace, to=self.room)
        return
