from sense_hat import SenseHat

sense = SenseHat()

import time

# sense = SenseHat()
green = (0, 255, 0)

def show_checkmark():
    sense.set_pixel(0, 0, green)


while(True):
    temp = sense.get_temperature_from_humidity()
    print("Temperature: %s C" % temp)
    show_checkmark()
    time.sleep(1)
    sense.clear()
    print("hey")