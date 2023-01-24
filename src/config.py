
import os
from dotenv import load_dotenv
load_dotenv()



class BaseConfig(object):
    PROJECT = "mmk-rt"
    PROJECT_ROOT = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    DEBUG = True
    TESTING = False
    SECRET_KEY = os.getenv('FLASK_SECRET')


class DefaultConfig(BaseConfig):
    DEBUG = True
    MONGO_URI = os.getenv('MONGO_URI', '')
    # REDIS_URL = os.getenv('REDIS_URL')

