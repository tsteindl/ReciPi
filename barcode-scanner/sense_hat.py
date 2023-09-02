from sense_hat import SenseHat
import time

sense = SenseHat()
green = (0, 255, 0)

def show_checkmark():
    sense.set_pixel(0, 0, green)

show_checkmark()
time.sleep(2)
sense.clear()