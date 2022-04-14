
import pyautogui
import cv2
import numpy as np
import random

debug = False

def cap(region=None):
    img = pyautogui.screenshot(region=region) if region else pyautogui.screenshot()
    # img = pyautogui.screenshot()
    # return np.asarray(img)
    # print(img)
    return cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR)
def cv_show(img, name = "debug") :
    cv2.imshow(name, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return

def match(template, img, value) :
    template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
    res = cv2.matchTemplate(img, template, cv2.TM_SQDIFF_NORMED)
    min, max, min_loc, max_loc = cv2.minMaxLoc(res)
    matchRes = False
    # if (value == 0.1) :
    if (min < value) :
        matchRes= True
    return matchRes, min_loc, min

def randomMs(min, max):
    return random.randint(min, max) / 1000

def randomS(min, max):
    return random.randint(min, max)
