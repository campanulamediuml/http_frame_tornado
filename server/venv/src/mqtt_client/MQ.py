from mqtt_client.client import mqtt_connection
from config import config
import time

class MQ(object):
    # mq_client = mqtt_connection(config.mqtt_server,1883,client_name='web_admin_server')

    @staticmethod
    def send_mqtt_info(mq_client,topic,payload,event_id):
        return mq_client.send_message(topic,payload,event_id)
    

    @staticmethod
    def get_send_result(mq_client,event_id):
        return mq_client.get_send_result(event_id)

    @staticmethod
    def disconnect(mq_client):
        return mq_client.disconnect()
   

    @staticmethod
    def send_data(topic,payload,event_id):
        event_id = str(event_id)
        mq_client = mqtt_connection(config.mqtt_server,1883,client_name='web_admin_server'+event_id)

        rec = MQ.send_mqtt_info(mq_client,topic,payload,event_id)
        if rec[0] != 0:
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




