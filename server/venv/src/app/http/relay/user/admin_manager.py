from data.server import Data
from config import config
from app.http.relay.user import user


import time

class UserManager(object):
    def __init__(self):
        self._player_dict = {}
        # 可以使用设备
        self._admin_dict = {}
        # 可以登录后台
        self._user_dict = {}

    def find_user_by_token(self,token):
        if token in self._user_dict:
            return self._user_dict[token]
        return None
    # 返回用户对象

    def get_all_user_dict(self):
        return self._user_dict

    def get_player_dict(self):
        return self._player_dict

    def get_admin_dict(self):
        return self._admin_dict

    def add_admin(self,access_token,user_id):
        self._admin_dict[access_token] = user_id
        self._user_dict[access_token] = user.User(user_id=user_id, user_role=config.admin_type, user_token=access_token, login_time=int(time.time()))
        return

    def add_player(self,access_token,user_id):
        self._player_dict[access_token] = user_id
        self._user_dict[access_token] = user.User(user_id=user_id, user_role=config.player_type, user_token=access_token, login_time=int(time.time()))
        return

    def get_admin_base(self,token):
        if token not in self._admin_dict:
            return 
        # 此人没登录
        admin_info = Data.find('openluat_user',[('id','=',admin_id)])
        return admin_info

    def get_player_base(self,token):
        if token not in self._player_dict:
            return 

        admin_info = Data.find('player',[('id','=',admin_id)])
        return player_info

    def is_god(self,token):
        if token not in self._admin_dict:
            return False
        if Data.find('openluat_user',[('openluat_user_id','=',admin_id)]) == None:
            return False
        return True

    def admin_logout(self,token):
        if token in self._admin_dict:
            self._admin_dict.pop(token)
        return

    def player_logout(self,token):
        if token in self._player_dict:
            self._player_dict.pop(token)
        return

    def user_logout(self,token):
        if token in self._user_dict:
            self._user_dict.pop(token)
        return
    # 登出




        
