import time

import thread as t
import cv2

import units
import client
import numpy as np


class Buff(t.ThreadController):
    bottom = []
    top = []
    key = {}
    topThresh = 100
    bottomThresh = 50
    def handle(self):
        isRun = self.check()
        if (isRun):
            self.lock.acquire()
            self.getAction().send(self.key)
            time.sleep(1.5)
            self.lock.release()
            time.sleep(10)
        time.sleep(1)

    def check(self):
        screen = self.getScreen()
        img = screen.get()
        img = img[0:100, 1200:2000]
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        ret1, thresh1 = cv2.threshold(img, self.bottomThresh, 255, cv2.THRESH_BINARY)
        res1 = units.match(self.bottom, thresh1, 0.1)
        #
        ret1, thresh2 = cv2.threshold(img, self.topThresh, 255, cv2.THRESH_BINARY)
        res2 = units.match(self.top, thresh2, 0.1)
        isRun = not res1[0] and not res2[0]
        if (units.debug):
            print(res1)
            units.cv_show(thresh1, "buff check")
            units.cv_show(self.bottom, "buff check")
            print(res2)
            units.cv_show(thresh2, "buff check")
            units.cv_show(self.top, "buff check")
        return isRun
    def setting(self, key:client.Key, top, bottom, topThresh = 100, bottomThresh = 50):
        self.key = key
        self.bottom = np.uint8(cv2.imread(bottom))
        self.top = np.uint8(cv2.imread(top))
        self.topThresh = topThresh
        self.bottom = bottomThresh
        return self

class Chance(t.ThreadController):
    def handle(self):
        self.lock.acquire()
        print("chance")
        time.sleep(0.8)
        self.getAction().send(client.Key("8", 700))
        self.lock.release()
        time.sleep(units.randomS(177, 180))

class Default(t.ThreadController):
    def handle(self):
        self.lock.acquire()
        time.sleep(0.8)
        self.getAction().send(client.Key("7", 1200))
        time.sleep(1.2)
        self.lock.release()
        time.sleep(units.randomS(177, 180))

class Warrior(t.ThreadController):
    def handle(self):
        self.lock.acquire()
        time.sleep(0.8)
        self.getAction().send(client.Key("7", 500))
        time.sleep(0.5)
        self.lock.release()
        time.sleep(units.randomS(880, 890))

class Eat(t.ThreadController):
    def handle(self):
        self.lock.acquire()
        time.sleep(0.8)
        # self.getAction().send(client.Key("3", 900))
        # time.sleep(0.9)
        self.getAction().send(client.Key("9", 700))
        time.sleep(1.7)
        self.lock.release()
        time.sleep(units.randomS(100, 120))
