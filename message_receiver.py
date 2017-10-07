import paho.mqtt.client as mqtt
import config_parser as config

class Receiver(object):
    def on_connect(self, client, userdata, flags, rc):
        client.subscribe(config.status_topic)
        self.led.red_led.blink(n=2)

    def on_message(self, client, userdata, msg):
        if msg.payload.decode() == 'OPEN':
            self.status = 'OPEN'
            print(self.status)
            self.led.for_open_door()
        elif msg.payload.decode() == 'CLOSED':
            self.status = 'CLOSED'
            print(self.status)
            self.led.for_closed_door()

    def __init__(self, led_control):
        self.status = None
        self.client = mqtt.Client()
        self.led = led_control

    def run(self):
        self.client.connect(config.base_ip, int(config.port), int(config.timeout))
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.loop_forever()
