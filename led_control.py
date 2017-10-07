from gpiozero import LED

class LedControl(object):
    def __init__(self):
        self.red_led = LED(20)
        self.green_led = LED(12)

    def for_open_door(self):
        self.green_led.on()
        self.red_led.off()

    def for_closed_door(self):
        self.red_led.on()
        self.green_led.off()

