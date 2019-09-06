from app.http.handler_base import HandlerBase
from app.http.relay.relay import Relay
from data.server import Data
import random
from ws_client.WS import WSIO,WSC
from tornado.concurrent import run_on_executor
from mqtt_client.MQ import MQ
from gevent import getcurrent

class mqtt_test(HandlerBase):
    @run_on_executor
    def get(self):

        event_id = id(getcurrent())

        mq_res = MQ.send_data('chat','from http',event_id)

        res = {
            'result':mq_res,
            'event_id':event_id
        }
        
        # res = Data.find('test',[('id','!=',0)])
        self.send_ok(res)
        return
