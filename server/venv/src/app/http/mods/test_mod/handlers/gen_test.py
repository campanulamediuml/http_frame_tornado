from app.http.handler_base import HandlerBase
from app.http.relay.relay import Relay
from data.server import Data
import json
import time
import requests
import random
from tornado.concurrent import run_on_executor
from common.common import get_event_id

class gen_test(HandlerBase):
    @run_on_executor
    def get(self):
        remote_ip = self.request.remote_ip
        if remote_ip != '127.0.0.1':
            return
            
        # join_time = int(time.time())
        Relay.add_admin(self.random_string())
        admin_dict = Relay.get_admin_dict()
        print('admin_dict',admin_dict,'from gen_test',id(admin_dict))
        # print('admin_dict',,'from gen_test')
        res = {
            'result':self.cal(),
            'gevent_id':get_event_id()
        }

        self.send_ok(res)
        return

    def cal(self):
        now_time = int(time.time())
        count = 0
        while 1:
            count += 1
            if int(time.time()) - now_time > 20:
                return count

    def random_string(self):
        res = ''
        for i in range(0,5):
            res+= random.choice('qwertyuiopasdfghjklzxcvbnm')

        return res

