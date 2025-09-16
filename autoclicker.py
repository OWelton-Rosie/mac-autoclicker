# autoclicker.py
# Run with: python3 autoclicker.py

import pyautogui
import time
from pynput import keyboard

clicking = False
running = True
cps = 60  # clicks per second (adjust if you like)
delay = 1 / cps

def on_press(key):
    global clicking, running
    try:
        if key.char == "s":  # toggle clicking
            clicking = not clicking
            print("Clicking:", clicking)
        elif key.char == "q":  # quit
            running = False
            return False
    except AttributeError:
        pass

listener = keyboard.Listener(on_press=on_press)
listener.start()

print("Autoclicker ready. Press 's' to start/stop, 'q' to quit.")

while running:
    if clicking:
        pyautogui.click()
        time.sleep(delay)  # caps CPU use
    else:
        time.sleep(0.05)  # idle efficiently
