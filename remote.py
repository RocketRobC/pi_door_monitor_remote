from gpiozero import LED, Button
from message_receiver import Receiver
from led_control import LedControl
from door_control import DoorControl
from signal import pause
import threading

led_control = LedControl()
receiver = Receiver(led_control)
door_control = DoorControl()

try:
    t = threading.Thread(target=receiver.run, daemon=True)
    t.start()
except:
    print('Status receiver failed to start')

door_control.button.when_released = door_control.send_command

pause()
