from app.http.handler_base import HandlerBase
from app.http.relay.relay import Relay
from data.server import Data
import random


class test(HandlerBase):
    def get(self):
        admin_dict = Relay.get_admin_dict()
        # admin_dict = Relay.get_admin_dict()
        print('admin_dict',admin_dict,'from test',id(admin_dict))
        res = Data.find('test',[('id','!=',0)])
        self.send_ok(res)
        return
