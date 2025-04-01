# Created by: Jack Eddy
# Created on: March 2025
#
# This program turns the LED on the pico on and off, increasing the time the light stays on each cycle

import time
import board
import digitalio

# variables
blink_time = 1

# sets LED pin to output
pin_3 = digitalio.DigitalInOut(board.GP3)
pin_4 = digitalio.DigitalInOut(board.GP4)
pin_5 = digitalio.DigitalInOut(board.GP5)
led.direction = digitalio.Direction.OUTPUT

# runs loop turning LED on for set time and off for set time, increases every cycle
while True:
    pin_3.value = True
    pin_4.value = False
    pin_5.value = False
    time.sleep(blink_time)
    pin_3.value = False
    pin_4.value = True
    pin_5.value = False
    time.sleep(blink_time)
    pin_3.value = False
    pin_4.value = False
    pin_5.value = True
    time.sleep(blink_time)
    pin_3.value = True
    pin_4.value = True
    pin_5.value = False
    time.sleep(blink_time)
    pin_3.value = True
    pin_4.value = False
    pin_5.value = True
    time.sleep(blink_time)
    pin_3.value = False
    pin_4.value = True
    pin_5.value = True
    time.sleep(blink_time)
    pin_3.value = True
    pin_4.value = True
    pin_5.value = True
    time.sleep(blink_time)0