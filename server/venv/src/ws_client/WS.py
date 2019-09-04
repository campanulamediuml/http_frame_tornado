from ws_client.ws_client import WS_connect
from config.config import push_config

server_url = 'ws://'+str(push_config['host'])+':'+str(push_config['port'])+'/socket.io/?EIO=3&transport=websocket'


class WSC(object):
    wsc = WS_connect(server_url)

    @staticmethod
    def send_data(code, content):
        return WSC.wsc.send_data(code, content)

    @staticmethod
    def get_result():
        return WSC.wsc.get_result()

    @staticmethod
    def update_result():
        return WSC.wsc.update_recer()
