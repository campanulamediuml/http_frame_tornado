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
        return

    def register_handles(self):
        WebSocketHandlers.register(self._sio)
        return

    def _update(self):
        IntervalTask(5, self.user_manager.update)
        return

    def send_msg(self, sid, code, data):
        self._sio.emit(code, data=msg, room=sid)
        return 
