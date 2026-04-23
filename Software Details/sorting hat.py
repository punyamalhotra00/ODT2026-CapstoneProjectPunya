from machine import Pin
from dfplayer import DFPlayer
import time
import random

A = Pin(25, Pin.IN, Pin.PULL_UP)
B = Pin(26, Pin.IN, Pin.PULL_UP)
C = Pin(27, Pin.IN, Pin.PULL_UP)
D = Pin(14, Pin.IN, Pin.PULL_UP)

def get_input():
    while True:
        if A.value()==0: time.sleep(0.2); return "A"
        if B.value()==0: time.sleep(0.2); return "B"
        if C.value()==0: time.sleep(0.2); return "C"
        if D.value()==0: time.sleep(0.2); return "D"
        
player = DFPlayer(1, 4, 5)  # UART1, TX=4, RX=5
time.sleep(1)
player.volume(25)




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
