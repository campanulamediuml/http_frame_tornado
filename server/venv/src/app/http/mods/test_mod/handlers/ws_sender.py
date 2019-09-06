from app.http.handler_base import HandlerBase
from ws_client.WS import WSIO,WSC
from tornado.concurrent import run_on_executor
import time
from gevent import getcurrent


class ws_sender(HandlerBase):
    @run_on_executor
    def get(self):
        print('收到信息',int(time.time()))
        data = {'info':'test'}
        result = {}
        event_id = id(data)
        print('本次请求的事件id位于tornado进程内id',event_id)
        result['event_id'] = event_id
        res = WSIO.send_data('req_test',data)
        if res == None:
            self.send_faild('WS_CONNECT_TIMEOUT')

        result['res'] = res
        result['gevent_id'] = id(getcurrent())
        self.send_ok(result)
        return

