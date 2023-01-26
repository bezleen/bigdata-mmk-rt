# --- Open cmt line bellow if run by cmd: python *.py
import sys  # nopep8
sys.path.append(".")  # nopep8
import csv
from pymongo import MongoClient

from src.config import DefaultConfig as Config


mongo_client = MongoClient(Config.MONGO_URI)["mmk"]
def sync_to_db():
    with open('scripts/data/valorant_mmk_for_db.csv', 'r') as f:
        csv_reader = csv.reader(f)
        warehouse = []
        for row in csv_reader:
            user_id = row[0]
            kd = row[1]
            kill = row[2]
            death = row[3]
            assistant = row[4]
            win_rate = row[5]
            pick_rate = row[6]
            avg_score = row[7]
            first_blood_rate = row[8]
            headshot_rate = row[10]
            record = {
                "user_id":user_id,
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
            warehouse.append(record)
            if len(warehouse)< 1000:
                continue
            # insert db
            mongo_client['player_rate'].insert_many(warehouse)
            # reset warehouse
            warehouse = []



if __name__ == '__main__':
    sync_to_db()