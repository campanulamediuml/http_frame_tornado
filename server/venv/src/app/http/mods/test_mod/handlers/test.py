from app.http.handler_base import HandlerBase
from data.server import Data

class test(HandlerBase):
    def get(self):
        res = Data.find('test',[('id','!=',0)])
        self.send_ok(res)
        return