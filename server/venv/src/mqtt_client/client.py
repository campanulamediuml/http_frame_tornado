import paho.mqtt.client as mqtt
import _thread as thread
import time

class mqtt_connection(object):

    def __init__(self,url,port,client_name):
        self.MQTTHOST = url
        self.MQTTPORT = port
        self.client_name = client_name
        self.mqttClient = mqtt.Client(client_id=self.client_name)
        self.msg_group = {}

    # 连接MQTT服务器
    def disconnect(self):
        print('http服务器断开mqtt链接')
        self.mqttClient.loop_stop()
        self.mqttClient.disconnect()

    def on_mqtt_connect(self):
        self.mqttClient.connect(self.MQTTHOST, self.MQTTPORT, 60)
        print('创建mqtt链接')
        return

    # publish 消息
    def on_publish(self,topic, payload, qos=1):
        res = self.mqttClient.publish(topic, payload, qos)
        return list(res)

    # 消息处理函数
    def on_message_come(self, lient, userdata, msg):
        print(msg.topic + " " + ":" + str(msg.payload))
        # print(int(time.time()))
        event_id = msg.topic.split('/')[-1]
        if event_id in self.msg_group:
            self.msg_group[event_id] = str(msg.payload)
            self.disconnect()
        return

    # subscribe 消息
    def on_subscribe(self,channel=None):
        self.mqttClient.subscribe("test_channel", 1)
        self.mqttClient.subscribe("/v1/device/+/+", 1)
        self.mqttClient.subscribe("/v1/device/+/+/+", 1)
        if channel != None:
            self.mqttClient.subscribe(channel+"/+", 1)
            print('加入',channel,'/+')
        self.mqttClient.on_message = self.on_message_come # 消息到来处理函数        
        # 加入监听

    def send_message(self,channel,data,event_id):
        # self.creat_connection()
        self.on_mqtt_connect()
        self.on_subscribe(channel)
        res = self.on_publish(channel+'/'+event_id,data)
        self.msg_group[event_id] = None
        self.mqttClient.loop_start()
        return res

    def get_send_result(self,event_id):
        if event_id not in self.msg_group:
            return None
        res = self.msg_group[event_id]
        self.msg_group[event_id] = None
        return res





# mqtt_connection('mq.aichihuo.vip',1883,client_name='web_admin_server')