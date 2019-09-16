from tornado.web import RequestHandler
from concurrent.futures import ThreadPoolExecutor
from app.http.error_code import ERROR_CODE
from data.server import Data
from app.http.relay.relay import Relay
from config import config
import json


class HandlerBase(RequestHandler):
    executor = ThreadPoolExecutor(20)

    def set_default_headers(self):
        self.set_header('Access-Control-Allow-Origin', '*')
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        self.set_header('Access-Control-Max-Age', 1000)
        self.set_header('Access-Control-Allow-Headers', '*')

    def get_result(self):
        '''
        返回结构基本模板
        :return:
        '''
        result = {}
        result['status'] = 0
        result['msg'] = ''
        result['data'] = {}
        return result


    def token_time_out(self):
        '''
        获取post请求内容
        :return:
        '''
        token = self.get_argument('token')
        Relay.token_time_out(token)
        return

    def get_admin_base(self):
        '''
        获取用户基本信息
        :return:
        '''
        # self.token_time_out()
        token = self.get_argument('token')
        res = Relay.get_admin_base(token)
        return res
        # return user_data

    def get_player_base(self):
        '''
        获取用户基本信息
        :return:
        '''
        # self.token_time_out()
        token = self.get_argument('token')
        res = Relay.get_player_base(token)
        return res


    def is_god(self):
        '''
        获取用户基本信息
        :return:
        '''
        token = self.get_argument('token')
        res = Relay.is_god(token)
        return res


    def player_logout(self):
        '''
        获取post请求内容
        :return:
        '''
        token = self.get_argument('token')
        res = Relay.player_logout(token)
        return res


    def admin_logout(self):
        '''
        获取post请求内容
        :return:
        '''
        token = self.get_argument('token')
        res = Relay.admin_logout(token)
        return res


    def send_ok(self, data = {}):
        '''
        正确信息返回
        :param data:
        :return:
        '''
        result = self.get_result()
        result['data'] = data
        self.write(result)

    def send_faild(self, code):
        '''
        失败信息返回
        :param code:
        :return:
        '''
        result = self.get_result()
        unit = ERROR_CODE[code]
        result['status'] = unit[0]
        result['msg'] = unit[1]
        self.write(json.dumps(result))

    def get_data(self):
        '''
        获取get请求内容
        :return:
        '''
        data = self.get_argument('data')
        res = json.loads(data)
        return res


    def get_post_data(self):
        '''
        获取post请求内容
        :return:
        '''
        data = json_decode(self.request.body)
        return res
















