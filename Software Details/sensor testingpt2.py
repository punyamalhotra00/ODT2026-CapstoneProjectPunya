from machine import I2C, Pin
import time

i2c = I2C(0, scl=Pin(21), sda=Pin(22))
MPU = 0x68

i2c.writeto_mem(MPU, 0x6B, b'\x00')

prev_ax = 0
prev_ay = 0

while True:
    data = i2c.readfrom_mem(MPU, 0x3B, 6)

    ax = (data[0] << 8) | data[1]
    ay = (data[2] << 8) | data[3]
    az = (data[4] << 8) | data[5]

    if ax > 32768: ax -= 65536
    if ay > 32768: ay -= 65536
    if az > 32768: az -= 65536

    # CHANGE (movement difference)
    dx = ax - prev_ax
    dy = ay - prev_ay

    # ---- GESTURES ----

    # 🪄 LIFT (slow upward)
    if az > 12000:
        print("FLOAT")

    # ⚡ DIAGONAL FLICK → DROP
    elif abs(dx) > 8000 and abs(dy) > 8000:
        print("DROP")

    # 🔄 CIRCLE DETECTION (basic)
    elif abs(dx) > 4000 and abs(dy) > 4000:
        print("SPIN")

    else:
        print("IDLE")

    prev_ax = ax
    prev_ay = ay

    time.sleep(0.15)
