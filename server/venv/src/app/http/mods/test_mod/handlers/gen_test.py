from app.http.handler_base import HandlerBase
from app.http.relay.relay import Relay
from data.server import Data
import json
import time
import requests




class gen_test(HandlerBase):
    def get(self):
        remote_ip = self.request.remote_ip
        if remote_ip != '127.0.0.1':
            return
            
        Relay.add_admin('1234','aaaa')
        print('admin_dict',Relay.get_admin_dict(),'from gen_test')
        res = {
            'result':self.cal()
        }

        self.send_ok(res)
        return

    def cal(self):
        now_time = int(time.time())
        count = 0
        while 1:
            count += 1
            if int(time.time()) - now_time > 10:
                return count
