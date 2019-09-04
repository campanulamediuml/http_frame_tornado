from websocket import create_connection
from threading import Timer, Thread
import json
import time
import _thread as thread

class WS_connect(object):
    def __init__(self, SERVER_URL):
        self.ws = create_connection(SERVER_URL)
        self.recer = []
        self.keep_connect()
        self.login_as_admin()

    def keep_connect(self):
        def run(*args):
            while 1:
                self.send_heart_beat()
                time.sleep(5)

        thread.start_new_thread(run, ())
        # 保持心跳
    def login_as_admin(self):
        self.send_data('ADMIN_IN', {})

    def send_heart_beat(self):
        self.ws.send('2')
        print('发送心跳包')
        self.update_result()

    def disconnect(self):
        self.ws.send('42' + json.dumps(['disconnect']))

    def send_data(self, code, content):
        data = '42' + json.dumps([code, content])
        self.ws.send(data)
        self.update_result()
        return self.get_result()

    def update_result(self):
        data = self.ws.recv()
        print('请求结果', data)
        if len(data) <= 2:
            if data == '3':
                print('heart_beat')
            return
        if data[:2] == '42':
            data_msg = json.loads(data[2:])
            self.recer = data_msg
            return self.get_result()

    def get_result(self):
        return self.recer
