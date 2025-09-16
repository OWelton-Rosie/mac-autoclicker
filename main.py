# Run with: python3 main.py

import pyautogui
import time
from pynput import keyboard

clicking = False
running = True
right_click = False  # start with left-click mode
cps = 15  # clicks per second (adjust as needed)
delay = 1 / cps

def on_press(key):
    global clicking, running, right_click
    try:
        if key.char == "s":  # toggle clicking
            clicking = not clicking
            print("Clicking:", clicking, "(Right)" if right_click else "(Left)")
        elif key.char == "r":  # toggle between left/right click
            right_click = not right_click
            print("Mode switched to:", "Right click" if right_click else "Left click")
        elif key.char == "q":  # quit
            running = False
            return False
    except AttributeError:
        pass

listener = keyboard.Listener(on_press=on_press)
listener.start()

print("Autoclicker ready.")
print("Press 's' to start/stop, 'r' to toggle left/right click, 'q' to quit.")

while running:
    if clicking:
        if right_click:
            pyautogui.click(button="right")
        else:
            pyautogui.click(button="left")
        time.sleep(delay)  # cap CPU use
    else:
        time.sleep(0.05)  # idle efficiently
