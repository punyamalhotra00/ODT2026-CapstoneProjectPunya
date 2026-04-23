from dfplayer import DFPlayer
import time

# Initialization (This part is working now!)
player = DFPlayer(1, 4, 5) 

print("Setting volume...")
player.volume(30)
time.sleep(0.5)

print("Playing track...")
# The library expects: player.play(folder_number, file_number)
player.play(1, 1)