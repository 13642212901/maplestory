import time

import thread
import cv2
import units
import numpy as np

class UserIndex(thread.ThreadController):
    point = cv2.imread("me.jpg")
    local = []
    def __init__(self):
        thread.ThreadController.__init__(self)
    def handle(self):
        cap = self.getScreen().get()
        res = self.checkPointInMap(cap, self.point, np.array([10, 160, 230]), np.array([110, 255, 255]))
        self.local = res[1]
        time.sleep(0.01)
    def checkPointInMap(self, img, point, lower, upper):
        img = img[0:200, 0:400]
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        inRange_hsv = cv2.inRange(hsv, lower, upper)
        thresh = cv2.bitwise_not(inRange_hsv)
        res = units.match(point, thresh, 0.02)
        return res
    def starting(self):
        self.isStart = 1
    def getX(self):
        return self.local[0]
    def getY(self):
        return self.local[1]
    def init(self):
        self.handle()
