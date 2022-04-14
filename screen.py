import time

import cv2

import thread as t
import units as u

class Screen(t.ThreadController):
    cap = []
    x = 0
    y = 0
    def __init__(self):
        t.ThreadController.__init__(self)
        self.findWindow()

    def findWindow(self):
        img = u.cap()
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        ret1, thresh = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)
        tpl = cv2.imread("icon.jpg")
        res1 = u.match(tpl, thresh, 0.01)
        if (res1[0]):
            self.x = res1[1][0] - 3
            self.y = res1[1][1] + 22
            print(self.x)
            print(self.y)
            self.handle()

    def handle(self):
        img = u.cap()
        img = img[self.y:self.y + 1080, self.x:self.x + 1920]
        self.cap = img
    def get(self):
        return self.cap