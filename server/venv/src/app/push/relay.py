from urllib import request
import json
import urllib
from threading import Timer
import traceback
from data.server import Data


class Relay(object):

    server = None
    user_manager = None

    @staticmethod
    def init(server):
        Relay.server = server
        Relay.user_manager = Relay.server.user_manager

    @staticmethod
    def send_msg(sid, code, data={}):
        # 发送消息
        return Relay.server.send_msg(sid, code , data)

    @staticmethod
    def send_disconnect(sid):
        return Relay.server.send_msg(sid, 'disconnect' , data=None)

    @staticmethod
    def update_status(sid):
        return Relay.user_manager.update_heart_beat(sid)

    # ==========和http服务器建立连接===========

    @staticmethod
    def connect_push_system(sid):
        return Relay.user_manager.add_admin(sid)

    @staticmethod
    def is_admin(sid):
        return Relay.user_manager.is_admin(sid)

    @staticmethod
    def kill_admin(sid):
        return Relay.user_manager.kill_admin(sid)

    @staticmethod
    def get_all_admin():
        return Relay.user_manager.get_all_admin()

    # ==========和http服务器建立连接===========

    
    @staticmethod
    def send_msg_by_user_id(user_id, code, data={}):
        # 通过user_id发消息
        user = Relay.get_user_by_user_id(user_id)
        if user == None:
            return
        return Relay.server.send_msg(user.get_sid(), code, data)

    @staticmethod
    def get_user_by_sid(sid):
        # 通过sid找到用户id
        return Relay.user_manager.get_user_by_sid(sid)

    @staticmethod
    def user_login(sid,user_id):
        return Relay.user_manager.login(sid,user_id)

    @staticmethod
    def get_user(user_id):
        return Relay.user_manager.get_user(user_id)

    @staticmethod
    def user_exit(user_id):
        user = Relay.get_user_by_id(user_id)
        return Relay.user_manager.user_exit(user_id)

    @staticmethod
    def send_error(sid):
        code = 'ACK_ERROR'
        data = {
            'msg':'请求被拒绝'
        }
        return Relay.send_msg(sid, code, data={})


   