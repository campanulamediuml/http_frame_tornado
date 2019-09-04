from app.push.socketio_base import SocketIOBase
from app.push.user.user_manager import UserManager
from app.push.relay import Relay
from app.push.cs_handler import WebSocketHandlers
from common.Scheduler import IntervalTask
import datetime


class GameServer(SocketIOBase):

    def __init__(self, host, port):
        SocketIOBase.__init__(self, host, port)
        self.user_manager = UserManager()

        Relay.init(self)  # 放在函数尾部

    def register_handles(self):
        WebSocketHandlers.register(self._sio)

    def _update(self):
        IntervalTask(1, self.user_manager.update)

    def send_msg(self, sid, code, msg):
        # user = Relay.get_user_by_sid(sid)
        # user_id = user.get_id()
        # print(user.get_nickname(), '|',user_id, "|",code , msg, datetime.datetime.now())
        # print(sid)
        self._sio.emit(code, data=msg, room=sid)
