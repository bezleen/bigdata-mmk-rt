
import pydash as py_


import src.functions as Funcs
import src.models.repo as Repo
from bson.objectid import ObjectId

class MMK(object):
    def __init__(self):
        pass
    def find_match(self, user_id):
        # input user id 

        # get user data from database
        player_rate_data = Repo.mPlayerRate.get_item_with({"_id":ObjectId("user_id")})
        print(player_rate_data)
        pass