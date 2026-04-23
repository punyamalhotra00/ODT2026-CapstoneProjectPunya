from machine import Pin
from dfplayer import DFPlayer
import neopixel
import time
import random
import network, espnow

# BUTTONS
A = Pin(34, Pin.IN, Pin.PULL_UP)
B = Pin(35, Pin.IN, Pin.PULL_UP)
C = Pin(18, Pin.IN, Pin.PULL_UP)
D = Pin(21, Pin.IN, Pin.PULL_UP)

def get_input():
    while True:
        if A.value()==0: time.sleep(0.2); return "A"
        if B.value()==0: time.sleep(0.2); return "B"
        if C.value()==0: time.sleep(0.2); return "C"
        if D.value()==0: time.sleep(0.2); return "D"


# NEOPIXEL RINGS
np1 = neopixel.NeoPixel(Pin(26), 16)
np2 = neopixel.NeoPixel(Pin(25), 16)
np3 = neopixel.NeoPixel(Pin(33), 16)

def all_off():
    for n in [np1,np2,np3]:
        n.fill((0,0,0))
        n.write()

# DC MOTORS
# DRIVER 1 → Motors 1 & 2
# DRIVER 2 → Motors 3 & 4
motors = [
    {"in1":Pin(23,Pin.OUT), "in2":Pin(22,Pin.OUT), "ena":PWM(Pin(27),freq=1000)},
    {"in3":Pin(21,Pin.OUT), "in4":Pin(19,Pin.OUT), "enb":PWM(Pin(14),freq=1000)},

]

# set same speed for all motors
def set_speed(duty=800):  # 0–1023
    for m in motors:
        m["ena"].duty(duty)
        m["enb"].duty(duty)
    

def lift_all():
    set_speed(800)
    for m in motors:
        m["in1"].value(1)
        m["in2"].value(0)
        m["in3"].value(1)
        m["in4"].value(0)
      

def drop_all():
    set_speed(600)
    for m in motors:
        m["in1"].value(0)
        m["in2"].value(1)
        m["in3"].value(0)
        m["in4"].value(1)
    
def stop_all():
    for m in motors:
        m["ena"].duty(0)
        m["enb"].duty(0)
       
def random_spin():
    chosen = random.sample(range(4),2)
    for i,m in enumerate(motors):
        m["ena"].duty(700)
        m["enb"].duty(700)
       
        if i in chosen:
            m["in1"].value(1)
            m["in2"].value(0)
            m["in3"].value(1)
            m["in4"].value(0)
           
        else:
            m["in1"].value(0)
            m["in2"].value(1)
            m["in3"].value(0)
            m["in4"].value(1)
          
# DF PLAYER
player = DFPlayer(1, 16, 17)  # UART1, TX=4, RX=5
time.sleep(1)
player.volume(25)

#ESPNOW
sta = network.WLAN(network.STA_IF)
sta.active(True)

e = espnow.ESPNow()
e.active(True)


#STAGE 1: SORTING HAT
input("Press ENTER to START")

gryff=sly=raven=huff=0

for i in range(1,6):
    player.play(1, i)
    time.sleep(6)

    ans = get_input()

    if i==1:
        if ans=="A": gryff+=3; huff+=1
        elif ans=="B": raven+=3; sly+=1
        elif ans=="C": sly+=3; raven+=1
        elif ans=="D": huff+=3; gryff+=1

    elif i==2:
        if ans=="A": gryff+=3; huff+=1
        elif ans=="B": raven+=3; sly+=1
        elif ans=="C": sly+=3; gryff+=1
        elif ans=="D": huff+=3; raven+=1

    elif i==3:
        if ans=="A": gryff+=3; sly+=1
        elif ans=="B": sly+=3; huff+=1
        elif ans=="C": raven+=3; huff+=1
        elif ans=="D": huff+=3; raven+=1

    elif i==4:
        if ans=="A": gryff+=3; raven+=1
        elif ans=="B": raven+=3; sly+=1
        elif ans=="C": sly+=3; gryff+=1
        elif ans=="D": huff+=3; raven+=1

    elif i==5:
        if ans=="A": gryff+=3; sly+=1
        elif ans=="B": raven+=3; huff+=1
        elif ans=="C": sly+=3; raven+=1
        elif ans=="D": huff+=3; gryff+=1

scores={"G":gryff,"S":sly,"R":raven,"H":huff}
house=max(scores,key=scores.get)

player.play(1,10)
time.sleep(2)

if house=="G": player.play(1,6)
elif house=="R": player.play(1,7)
elif house=="H": player.play(1,8)
elif house=="S": player.play(1,9)


#STAGE 2
input("Press ENTER for Stage 2")

for n in [np1,np2,np3]:
    n.fill((255,215,0)); n.write()

time.sleep(2)

choice=random.randint(0,2)
rings=[np1,np2,np3]

start=time.time()
while time.time()-start<5:
    rings[choice].fill((100,200,255))
    rings[choice].write()
    time.sleep(0.3)
    all_off()
    time.sleep(0.3)


#STAGE 3

input("Press ENTER for Stage 3")

while True:
    host,msg=e.recv()
    if msg:
        msg=msg.decode()

        if msg=="FLOAT":
            lift_all()

        elif msg=="DROP":
            drop_all()

        elif msg=="SPIN":
            random_spin()

        else:
            stop_all()

