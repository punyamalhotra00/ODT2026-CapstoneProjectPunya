from machine import Pin,PWM
import time

IN1 = Pin(22, Pin.OUT)
IN2 = Pin(23, Pin.OUT)
IN3 = Pin(21, Pin.OUT)
IN4 = Pin(19, Pin.OUT)
IN5 = Pin(18, Pin.OUT)
IN6 = Pin(5, Pin.OUT)
ena = PWM(Pin(15),freq=1000)
enb = PWM(Pin(12),freq=1000)
enc = PWM(Pin(13),freq=1000)


while True:
    
    # Rotate DC Motor in clockwise direction for 3 seconds with Speed 3 (Max Speed/RPM)
    ena.duty(1023)
    enb.duty(1023)
    enc.duty(1023)

    IN1.value(1) 
    IN2.value(0)
    IN3.value(1)
    IN4.value(0)
    IN5.value(1)
    IN6.value(0)
    time.sleep(3)
    print("working")
