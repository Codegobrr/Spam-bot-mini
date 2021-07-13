import time


import pyautogui
while True:
    time.sleep(1)
    f = open('r', "venv/beemovie")
    for word in f:
        pyautogui.typewrite(word)
        pyautogui.press("enter")
