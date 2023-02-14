import json
import uuid


import pydash as py_


import src.functions as Funcs
import src.models.repo as Repo
from bson.objectid import ObjectId
import src.constants as Consts
from flask_socketio import emit, join_room, disconnect
from src.extensions import socketio
from kafka import KafkaConsumer, KafkaProducer
import time


class MMK(object):
    def __init__(self, total_number_of_player_in_match=10, number_of_team_in_match=2, namespace=None):
        self.namespace = namespace
        self.total_number_of_player_in_match = total_number_of_player_in_match
        self.number_of_team_in_match = number_of_team_in_match
        # self.kafka_producer = KafkaProducer(bootstrap_servers=Consts.KAFKA_SERVER, value_serializer=lambda x: json.dumps(x).encode('utf-8'))
        self.dict_findings = {}
        """
        self.dict_findings = {
            "<user_id>": 1,
        }
        """
        self.pending = {}
        """
        self.pending = {
            "<tier_1>": [<user_id_1>, <user_id_2>, <user_id_3>,... ],
            "<tier_2>": [<user_id_5>, <user_id_4>, <user_id_6>,... ],
        }
        """
        self.test = []
        socketio.start_background_task(self.listen_kafka)

    def get_test(self, user_id):
        socketio.emit("test", self.test, namespace=self.namespace, to=user_id)
        return

    def listen_kafka(self):
        return
        self.kafka_consumer_pending = KafkaConsumer(
            Consts.TOPIC_PENDING,
            bootstrap_servers=[Consts.KAFKA_SERVER],
            auto_offset_reset='earliest',
            enable_auto_commit=True,
            group_id='my-group',
            value_deserializer=lambda x: json.loads(x.decode('utf8'))
        )
        for message in self.kafka_consumer_pending:
            message_data = message.value
            self.test.append(message_data)
            # TODO: get tier and user_id from message_data
            tier = py_.get(message_data, "tier")
            user_id = py_.get(message_data, "user_id")
            # handle the tier
            if not py_.get(self.pending, tier):
                py_.set_(self.pending, tier, [user_id])
                continue
            self.pending[tier].append(user_id)
            if len(self.pending[tier]) < self.total_number_of_player_in_match:
                continue
            match_users = self.pending[tier][:self.total_number_of_player_in_match]
            self.pending[tier] = self.pending[tier][self.total_number_of_player_in_match:]
            self.found_match(match_users)

    def find_match_demo(self, user_id, sid):
        socketio.emit("finding", {"user_id": user_id, "status": "finding", "req_id": sid}, namespace=self.namespace, to=user_id)
        time.sleep(3)
        match_id = uuid.uuid4().hex
        dict_team = {
            "team_1": [
                {
                    "user_id": "637f511a388719867cbf2721",
                    "display_name": "hien"
                },
                {
                    "user_id": "637f518c938013fd193f8620",
                    "display_name": "quang"
                },
                {
                    "user_id": "637f51df388719867cbf273b",
                    "display_name": "man"
                },
                {
                    "user_id": "637f53b1fcf69d51dd88c9f0",
                    "display_name": "nhan"
                }
            ],
            "team_2": [
                {
                    "user_id": "637f557e529b17316f8a7512",
                    "display_name": "hien2"
                },
                {
                    "user_id": "637f599e388719867cbf2771",
                    "display_name": "quang2"
                },
                {
                    "user_id": "47",
                    "display_name": "man2"
                },
                {
                    "user_id": "638025ecdbefe3eb478e4904",
                    "display_name": "nhan2"
                }
            ]
        }
        socketio.emit("found_match", {"match_id": match_id, "dict_team": dict_team}, namespace=self.namespace, to=user_id)
        return

    def found_match(self, user_ids):
        match_id = uuid.uuid4().hex
        dict_team = {}
        team_size = len(user_ids) // self.number_of_team_in_match
        for team_index in range(1, self.number_of_team_in_match + 1):
            start_index = int((team_index - 1) * team_size)
            stop_index = start_index + team_size
            team_data = {
                f"team_{team_index}": user_ids[start_index:stop_index]
            }
            dict_team.update(team_data)
        for user_id in user_ids:
            socketio.emit("found_match", {"match_id": match_id, "dict_team": dict_team}, namespace=self.namespace, to=user_id)
        return

    def find_match(self, user_id, sid):
        if False and py_.get(self.dict_findings, user_id) == 1:
            print(f"user {user_id} already in queue")
            return
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
        py_.set_(self.dict_findings, user_id, 1)
        # emit
        socketio.emit("finding", {"user_id": user_id, "status": "finding", "req_id": sid}, namespace=self.namespace, to=user_id)
        self.kafka_producer.send(Consts.TOPIC_FIND, value=record)
        # self.kafka_producer.send(Consts.TOPIC_PENDING, value=record)
        return
