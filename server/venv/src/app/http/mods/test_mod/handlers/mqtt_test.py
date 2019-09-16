from app.http.handler_base import HandlerBase
from app.http.relay.relay import Relay
from data.server import Data
import random
from ws_client.WS import WSIO,WSC
from tornado.concurrent import run_on_executor
from mqtt_client.MQ import MQ
from gevent import getcurrent
from common.common import get_event_id
import time

class mqtt_test(HandlerBase):
    @run_on_executor
    def get(self):

        # event_id = get_event_id()
        data = self.get_data()
        imei = data['imei']

        mq_res,info = MQ.send_start(imei)

        if mq_res == True:
        # res = Data.find('test',[('id','!=',0)])
            self.send_ok(mq_res)

        else:
            self.write(info)
        return
