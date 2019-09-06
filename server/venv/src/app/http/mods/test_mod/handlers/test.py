from app.http.handler_base import HandlerBase
from app.http.relay.relay import Relay
from data.server import Data
import random
from ws_client.WS import WSIO,WSC
from tornado.concurrent import run_on_executor



class test(HandlerBase):
    @run_on_executor
    def get(self):
        admin_dict = Relay.get_admin_dict()
        # admin_dict = Relay.get_admin_dict()
        print('admin_dict',admin_dict,'from test',id(admin_dict))
        res = Data.find('test',[('id','!=',0)])
        res['wsrc'] = WSC.get_wsrc_dict()
        self.send_ok(res)
        return
