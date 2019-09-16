from mqtt_client.client import mqtt_connection
from config import config
from common import common
from mgdb.mgdb import dbapi
import time
import json

class MQ(object):
    # mq_client = mqtt_connection(config.mqtt_server,1883,client_name='web_admin_server')

    @staticmethod
    def send_mqtt_info(mq_client,imei,topic,data):
        return mq_client.send_message(imei,topic,data)
    

    @staticmethod
    def get_send_result(mq_client,event_id):
        return mq_client.get_send_result(event_id)

    @staticmethod
    def disconnect(mq_client):
        return mq_client.disconnect()
   

    @staticmethod
    def send_data(imei,topic,data):
        # event_id = str(event_id)
        event_id = common.get_event_id()
        mq_client = mqtt_connection(config.mqtt_server,1883,event_id)

        rec = MQ.send_mqtt_info(mq_client,imei,topic,data)
        if rec == False:
            return None

        start_time = int(time.time())
        while 1:
            res = MQ.get_send_result(mq_client,event_id)
            if res != None:
                break
            time.sleep(0)
            if int(time.time()) -start_time >config.mq_time_out:
                break

        MQ.disconnect(mq_client)
        return res
        # 监听信息


    @staticmethod
    def send_start(imei,pulse=12,high=100,low=100):
        imei = imei
        pulse = 12
        money = pulse
        device_type = 1
        duration = 5
        high = high
        low  = low
        topic = 'deveventreq'

        data = bytearray([0x54, device_type])
        data += money.to_bytes(4, 'big')
        data += duration.to_bytes(4, 'big')
        data += high.to_bytes(4, 'big')
        data += low.to_bytes(4, 'big')
        data += pulse.to_bytes(4, 'big')
        print('发送的信号',data)

        mongodata = {
            'imei': imei,
            'datagram_type': 1,
            'device_type': device_type,
            'duration': duration,
            'high': high,
            'low': low,
            'pulse': pulse
        }

        result = MQ.send_data(imei,topic,data)
        if result and result['result']:
            mongodata['result'] = 0     # 成功
            dbapi.insert_datagram(mongodata)
            # device = dbapi.get_device(imei=imei)
            return True, json.dumps({'code': 0, 'msg': ''})
        else:
            mongodata['result'] = 1     # 设备正在运行
            dbapi.insert_datagram(mongodata)
            return False, json.dumps({'code': 8002, 'msg': '设备连接失败'})




