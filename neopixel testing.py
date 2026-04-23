from machine import Pin
import neopixel
import time

np1 = neopixel.NeoPixel(Pin(23),16)
np2 = neopixel.NeoPixel(Pin(5),16)

while True:
    for i in range(0, 16):
        # Set first neopixel to RED, and second neopixel to GREEN
        np1[i] = (255, 0, 0)
        np2[i] = (0, 255, 0)
    np1.write()
    np2.write()
    time.sleep(1)
    
    for i in range(0, 16):
        # Turn both neopixels off
        np1[i] = (0, 0, 0)
        np2[i] = (0, 0, 0)
        
    np1.write()
    np2.write()
    time.sleep(1)
    
 

    
    