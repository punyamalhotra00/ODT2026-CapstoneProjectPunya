from machine import UART, Pin
import time

# Create UART communication (Serial)
df = UART(2, baudrate=9600, tx=Pin(18), rx=Pin(19))

# Function to send command to DF Mini
def send_cmd(cmd, param):
    packet = bytearray([
        0x7E, 0xFF, 0x06, cmd, 0x00,
        (param >> 8) & 0xFF, param & 0xFF,
        0xFE, 0xEF
    ])
    df.write(packet)

# Set volume (0–30)
send_cmd(0x06, 25)

time.sleep(1)

# Play file 0001.mp3
send_cmd(0x03, 1)

questions = [1,2,3,4,5]

for q in questions:
    send_cmd(0x03, q)
    time.sleep(8)  # wait for audio to finish
    
score = 7  # example

if score <= 5:
    send_cmd(0x03, 7)  # raven
elif score <= 10:
    send_cmd(0x03, 6)  # gryff
elif score <= 15:
    send_cmd(0x03, 8)  # huff
else:
    send_cmd(0x03, 9)  # slyth
    
send_cmd(0x03, 10)

send_cmd(0x06, 25)

# play questions
for i in range(1,6):
    send_cmd(0x03, i)
    time.sleep(8)

# play effect
send_cmd(0x03, 10)
time.sleep(2)

# play result
send_cmd(0x03, 6)  # gryff example
