from machine import Pin
import time

btn1 = Pin(18, Pin.IN, Pin.PULL_UP)
btn2 = Pin(19, Pin.IN, Pin.PULL_UP)
btn3 = Pin(21, Pin.IN, Pin.PULL_UP)
btn4 = Pin(22, Pin.IN, Pin.PULL_UP)

while True:
    if not btn1.value():
        print("Button A pressed")
        time.sleep(0.3)

    if not btn2.value():
        print("Button B pressed")
        time.sleep(0.3)

    if not btn3.value():
        print("Button C pressed")
        time.sleep(0.3)

    if not btn4.value():
        print("Button D pressed")
        time.sleep(0.3)
