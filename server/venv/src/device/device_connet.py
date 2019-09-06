import paho.mqtt.client as MQTT
from config import config


class mqtt_method(object):
    mqtt_client = None
    listen_event_dict = {}

    @staticmethod
    def on_subscribe():
        mqtt_method.mqtt_client.subscribe("/v1/device/+/deveventrsp/+")
        dbg("subscribe result = {}".format(re))
        re = mqtt_client.subscribe("/v1/+/c_trans")
        dbg("subscribe result = {}".format(re))
     


