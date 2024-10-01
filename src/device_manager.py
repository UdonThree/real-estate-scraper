import time
import pyautogui

pyautogui.FAILSAFE = False


def get_current_position():
    for i in range(3):
        print(str(i))
        time.sleep(1)
    xy = pyautogui.position()
    print(xy.x)
    print(xy.y)


def move_to_button():
    pyautogui.moveTo(1464, 1459, 0.5)


def click_left_button():
    pyautogui.click()
