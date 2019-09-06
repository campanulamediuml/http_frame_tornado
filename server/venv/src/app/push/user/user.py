from data.server import Data
from app.push.relay import Relay
import time
import json

class User(object):

    def __init__(self, user_id):
        self._id = user_id
        self._sid = 0
        self._heartbeat_time = int(time.time())

    def update_heartbeat_time(self):
        """
        更新心跳
        :return:
        """
        self._heartbeat_time = time.time()

    def has_heartbeat(self):
        if time.time() - self._heartbeat_time > 15:
            return False

        return True

    def init_from_data(self,sid):  
        self._sid = sid

    def get_sid(self):
        return self._sid

    def update_heart_beat(self):
        self._heartbeat_time = int(time.time())

        