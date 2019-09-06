from ws_client.ws_client import WS_connect
# from ws_client.WSRC import WSRC
from config.config import push_config
from config import config
import json
import time
# import asyncio
import _thread as thread


server_url = 'ws://'+str(push_config['client_host'])+':'+str(push_config['port'])+'/socket.io/?EIO=3&transport=websocket'
print(server_url)

class WSC(object):
    wsc = WS_connect(server_url)

    @staticmethod
    def send_data(code, content):
        return WSC.wsc.send_data(code, content)

    @staticmethod
    def get_data_by_event_id(event_id):
        return WSC.wsc.get_data_by_event_id(event_id)

    @staticmethod
    def get_wsrc_dict():
        return WSC.wsc.get_wsrc_dict()



class WSIO(object):
    # 重写IO
    @staticmethod
    def send_data(code,data,event_id):
    # 协程函数
        # def run(*args):
        # event_id = 
        print('本次请求的事件id',event_id)
        data['server_token'] = event_id
        
        send_status = WSC.send_data(code,data)
        if send_status != True:
            return None
        # 无法发送

        time_wait_start = int(time.time())
        while 1:
            res = WSC.get_data_by_event_id(event_id)
            if res != None: 
                return res
            time.sleep(0)
            if int(time.time()) - time_wait_start > config.ws_time_out:
                break
        return res

        # res = thread.start_new_thread(run, (code,data))
        # return res
        # 超时





