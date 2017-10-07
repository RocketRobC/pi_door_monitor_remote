import paho.mqtt.client as mqtt
import config_parser as config
from gpiozero import Button

class DoorControl(object):
    def __init__(self):
        self.button = Button(25)
        self.client = mqtt.Client()
        self.client.connect(config.base_ip, int(config.port))

    def send_command(self):
        self.client.publish(config.door_control_topic, 'trigger')

