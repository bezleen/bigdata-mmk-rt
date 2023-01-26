# --- Open cmt line bellow if run by cmd: python *.py
import sys  # nopep8
sys.path.append(".")  # nopep8

from pymongo import MongoClient

from src.config import DefaultConfig as Config


mongo_client = MongoClient(Config.MONGO_URI)["mmk"]
