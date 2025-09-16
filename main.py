# for installation instructions, see README.md

import pyautogui
import time
from pynput import keyboard
from datetime import datetime

clicking = False
running = True
right_click = False  # start with left-click mode

# --- CPS setup ---
while True:
    try:
        cps = float(input("Enter clicks per second (CPS): "))
        if cps <= 0:
            raise ValueError
        break
    except ValueError:
        print("Please enter a positive number for CPS.")

delay = 1 / cps

def log(message):
    """Prints a nicely formatted log message with timestamp."""
    now = datetime.now().strftime("%H:%M:%S")
    print(f"[{now}] {message}")

def on_press(key):
    global clicking, running, right_click
    try:
        if key.char == "s":  # toggle clicking
            clicking = not clicking
            if clicking:
                log(f"Clicking started ({'Right' if right_click else 'Left'}) at {cps} CPS")
            else:
                log("Autoclicker paused")
        elif key.char == "r":  # toggle between left/right click
            right_click = not right_click
            log(f"Mode switched to: {'Right click' if right_click else 'Left click'}")
        elif key.char == "q":  # quit
            running = False
            log("Autoclicker stopped. Exiting program.")
            return False
    except AttributeError:
        pass

listener = keyboard.Listener(on_press=on_press)
listener.start()

log("Autoclicker ready")
print("Controls: [s] start/stop  |  [r] toggle left/right  |  [q] quit")

while running:
    if clicking:
        pyautogui.click(button="right" if right_click else "left")
        time.sleep(delay)  # cap CPU use
    else:
        time.sleep(0.05)  # idle efficiently
