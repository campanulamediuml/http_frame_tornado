from app.http.handler_base import HandlerBase
from app.http.relay.relay import Relay
from tornado.concurrent import run_on_executor
from common.common import get_event_id

from data.server import Data



class test(HandlerBase):
    @run_on_executor
    def get(self):

        res = {
            'event_id':get_event_id()
        }
        
        # res = Data.find('test',[('id','!=',0)])
        self.send_ok(res)
        return
