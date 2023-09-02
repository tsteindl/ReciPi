from sense_hat import SenseHat
import time

sense = SenseHat()
green = (0, 255, 0)

def show_checkmark():
    sense.set_pixel(0, 0, green)

while(True):
    show_checkmark()
    time.sleep(1)
    sense.clear()