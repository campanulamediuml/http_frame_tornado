import time
import json
from common import common
from data.server import Data

from app.http.relay.user import user_manager 


class Relay(object):
    server = None
    user_manager = user_manager.UserManager()
    # player_manager = user_manager.UserManager()
    
    @staticmethod
    def init(server):
        Relay.server = server
        # 创建初始用户

# 服务器核心操作放在这里
    @staticmethod
    def test():
        pass

    @staticmethod
    def get_admin_dict():
        # 获取全部admin字典
        return Relay.user_manager.get_admin_dict()

    @staticmethod
    def get_player_dict():
        # 获取全部player字典
        return Relay.user_manager.get_player_dict()

    @staticmethod
    def add_player(token,user_id):
        # 添加在线player
        return Relay.user_manager.add_player(token,user_id)

    @staticmethod
    def add_admin(token,user_id):
        # 添加在线admin
        return Relay.user_manager.add_admin(token,user_id)

    @staticmethod
    def get_admin_base(token):
        # 根据token获取admin信息
        return Relay.user_manager.get_admin_base(token)

    @staticmethod
    def get_player_base(token):
        # 根据token获取player信息
        return Relay.user_manager.get_player_base(token)

    @staticmethod
    def is_god(token):
        # 判断是不是超级管理员
        return Relay.user_manager.is_god(token)

    @staticmethod
    def player_logout(token):
        Relay.user_manager.user_logout(token)
        return Relay.user_manager.player_logout(token)
        # player推出

    @staticmethod
    def admin_logout(token):
        Relay.user_manager.user_logout(token)
        return Relay.user_manager.admin_logout(token)
        # admin退出

    @staticmethod
    def user_time_out(token):
        Relay.player_logout(token)
        Relay.admin_logout(token)
        Relay.user_manager.user_logout(token)
        return

