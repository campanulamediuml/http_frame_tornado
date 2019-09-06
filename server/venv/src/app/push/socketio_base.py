from flask_socketio import socketio
import eventlet.wsgi
from flask import Flask
from common.Scheduler import Scheduler


def index():
    print(1111)
    return ("1111")

def connect(sid, environ):
    print(sid, environ)
    print(2222222222);

class SocketIOBase(object):

    def __init__(self, host, port):
        self._host = host
        self._port = port
        self._sio = socketio.Server()
        self._app = Flask(__name__)

    def register_handles(self):
        self._app.route('/index')(index)
        self._sio.on('connect', namespace='/')(connect)

    def scheduler(self):
        Scheduler.run()
        eventlet.spawn_after(1, self.scheduler)

    def run(self):
        self.register_handles()
        app = socketio.Middleware(self._sio, self._app)
        self._update()
        eventlet.spawn_after(5, self.scheduler)
        eventlet.wsgi.server(eventlet.listen((self._host, self._port)), app, log_output=False)

    def _update(self):
        pass

    def get_host(self):
        return self._host

    def get_port(self):
        return self._port


# if __name__ == '__main__':
#     server = SocketIOBase('192.168.1.108', 9001)
#     server.run()