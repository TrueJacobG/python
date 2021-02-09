import time
import pyautogui

time.sleep(5)

tekst = open('./spam_bot/tekst-tutaj.txt', 'r')

for linijka in tekst:
    for slowo in linijka.split():
        pyautogui.typewrite(slowo)
        pyautogui.press("enter")
