from src.extensions import mdb
from .player_rate import PlayerRateDAO

mPlayerRate = PlayerRateDAO(mdb.db.player_rate)
