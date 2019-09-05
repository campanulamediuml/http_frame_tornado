import time
import json
from common import common
from data.server import Data
from config import config
from common.Scheduler import IntervalTask




class Relay(object):
    server = None
    player_token_dict = {}
    admin_token_dict = {}
    
    @staticmethod
    def init(server):
        Relay.server = server
        # 创建初始用户
        Relay.token_refresh()

# 服务器核心操作放在这里
    @staticmethod
    def test():
        pass

    @staticmethod
    def token_refresh():
        IntervalTask(5, Relay.kill_token)

    @staticmethod
    def kill_token():
        Relay.remove_time_out_token(Relay.player_token_dict,'player')
        Relay.remove_time_out_token(Relay.admin_token_dict,'openluat_user')
        return
        
    @staticmethod
    def remove_time_out_token(user_dict,connect_table):
        now_time = int(time.time())
        pop_list = []
        for token in user_dict:
            if now_time - user_dict[token] > config.token_time_out:
                pop_list.append(token)

        for token in pop_list:
            user_dict.pop(token)
            Data.update(connect_table,[('token','=',token)],{'token':''})
        return

    @staticmethod
    def get_admin_dict():
        return Relay.admin_token_dict

    @staticmethod
    def add_admin(token):
        join_time = int(time.time())
        Relay.admin_token_dict[token] = join_time
        return





