import paho.mqtt.client as mqtt
import _thread as thread
import time

class mqtt_connection(object):

    def __init__(self,url,port,token):
        self.MQTTHOST = url
        self.MQTTPORT = port
        self.token = token
        self.mqttClient = mqtt.Client(client_id='tornado_server'+'_'+token)
        self.msg_group = {}
        self.result = {
            self.token:None
        }

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
    def on_message_come(self, client, userdata, msg):
        print(msg.topic + " " + ":" + str(msg.payload))
        items = msg.topic.split('/')
        if len(items) > 4 and items[4] == "deveventrsp":
            token = items[5]
            if msg.payload[0] == 0xc:  # protocol 3.15
                if msg.payload[1] == 0x54:  # payment notification
                    data = {}
                    # [2] result
                    data['result'] = msg.payload[2]
                    if token in self.result:
                        self.result[token] = data
                        print(token,'收到消息',data)
                        self.disconnect()
        return


    def publish_mqtt_msg(self,topic, msg, qos=0):
        print("publish_mqtt_msg topic = %s" % (topic))
        result, mid = self.mqttClient.publish(topic, msg, qos=qos)
        if result != mqtt.MQTT_ERR_SUCCESS:
            print("error result %d, mid %d" % (result, mid))
            return False
        print("success result %d, mid %d" % (result, mid))
        return True


    def send_to_dev(self,imei,topic,data):
        mqtt_result = self.publish_mqtt_msg("/v1/device/{0}/{1}/{2}".format(imei, topic, self.token), data)
        return mqtt_result


    # subscribe 消息
    def on_subscribe(self):
        self.mqttClient.subscribe("/v1/device/+/deveventrsp/+")
        print('加入监听频道，监听机器回调')
        self.mqttClient.subscribe("/v1/device/+/+", 1)
        self.mqttClient.subscribe("/v1/device/+/+/+", 1)
        self.mqttClient.on_message = self.on_message_come # 消息到来处理函数        
        # 加入监听

    def send_message(self,imei,topic,data):
        # self.creat_connection()
        self.on_mqtt_connect()
        self.on_subscribe()
        # res = self.on_publish(channel+'/'+event_id,data)

        res = self.send_to_dev(imei,topic,data)
        
        self.mqttClient.loop_start()
        return res

    def get_send_result(self,token):
        if token in self.result:
            res =  self.result[token]
        else:
            res =  None
        self.result[token] = None
        return res





# mqtt_connection('mq.aichihuo.vip',1883,client_name='web_admin_server')