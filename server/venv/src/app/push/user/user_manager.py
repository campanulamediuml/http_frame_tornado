from app.push.user.user import User
from app.push.relay import Relay
from data.server import Data
import time

class UserManager(object):
    def __init__(self):
        self._user_dict = {}
        self._user_handler_dict = {}
        self._admin_list = []

    def update(self):
        del_list = list()
        for user_id, user in self._user_dict.items():
            if user.has_heartbeat() is True:
                continue
            del_list.append(user_id)

        for user_id in del_list:
            Relay.user_exit(user_id)
        # 更新用户管理器

        # print(self._admin_list)
    def get_user(self,user_id):
        if user_id in self._user_dict:
            return self._user_dict[user_id]
        return None

    def add_admin(self,sid):
        self._admin_list.append(sid)
        return

    def is_admin(self,sid):
        if sid in self._admin_list:
            return True
        return False
        # 后台链接

    def kill_admin(self,sid):
        if sid in self._admin_list:
            self._admin_list.remove(sid)
        return
        # 清除admin
    # =============管理后台链接=============

    def login(self,user_id):
        user = self.create_user(user_id)
        # 注册用户信息
        self._user_dict[user_id] = user
        self._user_handler_dict[sid] = user
        return

    def create_user(self,user_id):
        user = User(user_id)
        user.init_from_data(sid)
        return
        # 创建用户

    def get_user_by_sid(self,sid):
        if sid in self._user_handler_dict:
            return self._user_handler_dict[sid]
        else:
            return None
        # 通过sid获取用户

    def user_exit(self,user_id):
        # 玩家退出
        user = self._user_dict[user_id]

        if user_id in self._user_dict:
            self._user_dict.pop(user_id)

        if user.get_sid() in self._user_handler_dict:
            self._user_handler_dict.pop(user.get_sid())

        return




