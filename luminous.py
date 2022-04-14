import time

import client
import thread
import units
import user
import cv2


class Luminous(user.User):
    type = 1
    attKey = "w"
    checkStart = 0
    flashTime = 1
    returnTime = 6

    def att(self):
        if (self.checkStart == 0):
            self.ac = AttCheck(self)
            self.ac.setScreen(self.getScreen())
            self.ac.starting()
            self.ac.start()
        self.getAction().send(client.Key(self.attKey))
        time.sleep(units.randomMs(750, 800))
    def handle(self):
        self.lock.acquire()
        if (self.type == 1):
            self.oneMap()
        self.lock.release()
        time.sleep(0.5)
    def useOneMap(self):
        self.type = 1
    def setAttKey(self, k):
        self.attKey = k
    def setAttTime(self, t):
        self.attTime = t
    def getAttKey(self):
        return self.attKey
    def buffTpl(self):
        return ["luminous/buff_top1.jpg", "luminous/buff_bottom1.jpg", 100, 50]

class AttCheck(thread.ThreadController):
    def __init__(self, luminous):
        thread.ThreadController.__init__(self)
        self.luminous = luminous
        self.lightTpl = cv2.imread("luminous/light.jpg")
        self.darkTpl = cv2.imread("luminous/dark.jpg")
        self.eqTpl = cv2.imread("luminous/eq.jpg")

    def handle(self):
        thread.runeLock.acquire()
        isLight = self.check(self.lightTpl)
        if (isLight[0]):
            self.luminous.setAttKey("e")
            self.luminous.setAttTime(3)
            if (not self.luminous.getAttKey() == "e"):
                thread.runeLock.release()
                time.sleep(10)
        isDark = self.check(self.darkTpl)
        if (isDark[0]):
            self.luminous.setAttKey("w")
            self.luminous.setAttTime(2)
            if (not self.luminous.getAttKey() == "w"):
                thread.runeLock.release()
                time.sleep(10)
        isEq = self.check(self.eqTpl)
        if (isEq[0]):
            self.luminous.setAttKey("r")
            self.luminous.setAttTime(1)
            if (not self.luminous.getAttKey() == "r"):
                thread.runeLock.release()
                time.sleep(10)
        thread.runeLock.release()
        time.sleep(0.3)

    def check(self, tpl):
        img = self.getScreen().get()
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img = img[450:700, 380:450]
        ret1, thresh = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY)
        res = units.match(tpl, thresh, 0.05)
        return res
