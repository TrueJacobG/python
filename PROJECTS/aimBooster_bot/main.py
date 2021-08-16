import pyautogui
import time
import keyboard
import random
import win32api
import win32con

time.sleep(2)


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

# record: 1:45


while keyboard.is_pressed("q") == False:
    img = pyautogui.screenshot(region=(530, 370, 840, 600))
    width, heigth = img.size

    for x in range(0, width, 5):
        for y in range(0, heigth, 5):
            r, g, b = img.getpixel((x, y))

            if b == 195:
                pyautogui.click(x+530, y+370)
                break
