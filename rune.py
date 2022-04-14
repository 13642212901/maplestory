import client
import thread
import units as u
import cv2
import copy
import time
import numpy as np
import copy
import winsound

import user

SORT_MODE_X = 1
SORT_MODE_Y = 2

class RuneUse:
    def __init__(self, cap):
        self.cap = cap
        self.c = copy.copy(self.cap)
        self.img = []

    def handelCap(self):
        # gray = cv2.cvtColor(self.cap, cv2.COLOR_BGR2GRAY)
        # ret1, thresh = cv2.threshold(gray, 75, 255, cv2.THRESH_BINARY_INV)
        # tpl = cv2.imread("rune/box_left.jpg")
        # res = u.match(tpl, thresh, 0.01)
        # x = res[1][0]
        # y = res[1][1]
        # img = self.cap[y:y + 82, x:x + 400]
        img = self.cap[175:300, 600:1360]
        self.img = img
        if (u.debug):
            u.cv_show(img, "22")
        # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        b, g, r = cv2.split(img)
        # gray = cv2.cvtColor(r, cv2.COLOR_BGR2GRAY)
        # cv_show(gray, "22")
        ret1, thresh1 = cv2.threshold(r, 185, 255, cv2.THRESH_BINARY)
        ret, thresh2 = cv2.threshold(g, 200, 255, cv2.THRESH_BINARY)
        thresh = cv2.add(thresh1, thresh2)

        # 膨胀两次填补缺口
        thresh = cv2.dilate(thresh, np.ones((2, 2), np.uint8))
        thresh = cv2.dilate(thresh, np.ones((2, 2), np.uint8))

        thresh = cv2.bitwise_not(thresh)
        # u.cv_show(thresh, "22")
        return thresh

    def getContourArrows(self, thresh):
        out, contours, hi = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        arrows = []
        for cnt in range(len(contours)):
            epsilon = 0.03 * cv2.arcLength(contours[cnt], True)
            approx = cv2.approxPolyDP(contours[cnt], epsilon, True)
            area = int(cv2.contourArea(contours[cnt]))
            if (int(area) > 330 and int(area) < 560 and len(approx) > 5 and len(approx) < 9):
                arrows.append(approx)
                print(len(approx), int(area), "success")
                for rox in approx:
                    # print(rox[0])
                    cv2.circle(self.img, (rox[0][0], rox[0][1]), 2, (0, 0, 255), 4)
            else:
                print(len(approx), int(area), "error")
                if (len(approx) > 3 and len(approx) < 9):
                    for rox in approx:
                        # print(rox[0])
                        cv2.circle(self.img, (rox[0][0], rox[0][1]), 2, (0, 0, 255), 4)
        return arrows

    def sortArrows(self, arrows):
        for i in range(1, len(arrows)):
            for o in range(0, len(arrows) - i):
                if arrows[o][0][0][0] > arrows[o+1][0][0][0]:
                    arrows[o], arrows[o+1] = arrows[o+1], arrows[o]
        return arrows

    #mode = MODE_X 按x轴排序 其他 y 轴
    def sortPointsByMode(self, mode, points):
        for i in range(1, len(points)):
            for o in range(0, len(points) - i):
                if (mode == SORT_MODE_X):
                    gt = points[o][0][0] > points[o + 1][0][0]
                else:
                    gt = points[o][0][1] > points[o + 1][0][1]
                if gt:
                    b = copy.copy(points[o])
                    points[o] = copy.copy(points[o + 1])
                    points[o + 1] = copy.copy(b)
        return points

    def discernDirection(self, arrows):
        result = []
        for arrow in arrows:
            arrow = self.sortPointsByMode(SORT_MODE_X, arrow)
            left = arrow[1][0][0] - arrow[0][0][0]
            right = arrow[len(arrow) - 1][0][0] - arrow[len(arrow) - 2][0][0]
            if (left > right):
                x = left
            else:
                x = right
            arrow = self.sortPointsByMode(SORT_MODE_Y, arrow)
            up = arrow[1][0][1] - arrow[0][0][1]
            down = arrow[len(arrow) - 1][0][1] - arrow[len(arrow) - 2][0][1]
            if (up > down):
                y = up
            else:
                y = down
            if (x > y):
                if (left > right):
                    result.append(client.Key("left"))
                else:
                    result.append(client.Key("right"))
            else:
                if (up > down):
                    result.append(client.Key("up"))
                else:
                    result.append(client.Key("down"))
        return result
    def use(self, test = 0):
        thresh = self.handelCap()
        arrows = self.getContourArrows(thresh)
        arrows = self.sortArrows(arrows)
        result = self.discernDirection(arrows)
        if (test == 0):
            cv2.imwrite("rune_log/" + str(int(time.time())) + ".jpg", self.img)
            cv2.imwrite("rune_log/" + str(int(time.time())) + "copy.jpg", self.c)
        else:
            for k in result:
                print(k.key)
            u.cv_show(self.img, "22")
        # u.cv_show(self.img, "rune point")
        if (len(result) < 4):
            result = []
        return result
    def success(self):
        return True

class RuneCheck(thread.ThreadController):
    now = 0
    checkTime = 0
    def __init__(self, userObj:user.User):
        thread.ThreadController.__init__(self)
        self.userObj = userObj
    def checkPointInMap(self, point, lower, upper):
        img = self.getScreen().get()
        img = img[0:150, 0:300]
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        inRange_hsv = cv2.inRange(hsv, lower, upper)
        thresh = cv2.bitwise_not(inRange_hsv)
        res = u.match(point, thresh, 0.02)
        return res
    def changeCH(self):
        self.getAction().send(client.Key("w Up", 300))
        time.sleep(0.05)
        self.getAction().send(client.Key("left Up", 300))
        time.sleep(0.05)
        self.getAction().send(client.Key("left Right", 300))
        time.sleep(15)
        self.getAction().send(client.Key("esc", 300))
        time.sleep(0.5)
        self.getAction().send(client.Key("Enter", 300))
        time.sleep(0.5)
        self.getAction().send(client.Key("right", 300))
        time.sleep(0.5)
        self.getAction().send(client.Key("Enter", 3000))
        time.sleep(3)
        self.getAction().send(client.Key("esc", 300))
        time.sleep(0.5)
        self.getAction().send(client.Key("Enter", 300))
        time.sleep(0.5)
        self.getAction().send(client.Key("right", 300))
        time.sleep(0.5)
        self.getAction().send(client.Key("Enter", 300))
        time.sleep(15)
        self.userObj.back()

    def handle(self):
        runePoint = cv2.imread("has_rune.jpg")
        runeRes = self.checkPointInMap(runePoint, np.array([110, 70, 200]), np.array([255, 170, 255]))
        if (runeRes[0]):
            duration = 1000  # millisecond
            freq = 440  # Hz
            winsound.Beep(freq, duration)
            time.sleep(10)
            return
            # time.sleep(240)
            # self.lock.acquire()
            # self.changeCH()
            # self.lock.release()
            # return
            self.checkTime = self.checkTime + 1
            if ((int(time.time()) - self.now) < 10 and self.checkTime > 2):
                self.stoping()
                return
            thread.runeLock.acquire()
            self.lock.acquire()
            time.sleep(4)
            point = cv2.imread("me.jpg")
            meRes = self.checkPointInMap(point, np.array([10, 160, 230]), np.array([110, 255, 255]))
            runeLoc = runeRes[1]
            meLoc = meRes[1]
            xDiff = runeLoc[0] - meLoc[0]
            if (abs(xDiff) > 3):
                if (xDiff > 0):
                    # right
                    self.userObj.right()
                    direction = 2
                else:
                    # left
                    self.userObj.left()
                    direction = 1
                runeRes = self.checkPointInMap(runePoint, np.array([110, 70, 200]), np.array([255, 170, 255]))
                meRes = self.checkPointInMap(point, np.array([10, 160, 230]), np.array([110, 255, 255]))
                i = 0
                print("move start")
                while runeRes[0] and abs(runeRes[1][0] - meRes[1][0]) > 5:
                    time.sleep(0.002)
                    if (i > 40):
                        return
                    runeRes = self.checkPointInMap(runePoint, np.array([110, 70, 200]), np.array([255, 170, 255]))
                    meRes = self.checkPointInMap(point, np.array([10, 160, 230]), np.array([110, 255, 255]))
                print("move stop")
                if (direction == 1):
                    # left stop
                    self.userObj.leftStop()
                    time.sleep(0.5)
                    self.userObj.left()
                    time.sleep(0.3)
                    self.userObj.leftStop()
                else:
                    self.userObj.rightStop()
                    time.sleep(0.5)
                    self.userObj.right()
                    time.sleep(0.3)
                    self.userObj.rightStop()
                    # right stop

                time.sleep(0.4)
                yDiff = runeRes[1][1] - meRes[1][1]
                i = 0
                print(yDiff)
                while runeRes[0] and abs(yDiff) > 6:
                    if (i > 40):
                        return
                    if (yDiff > 0):
                        self.userObj.down()
                        direction = 2
                    else:
                        self.userObj.up()
                        direction = 1
                    runeRes = self.checkPointInMap(runePoint, np.array([110, 70, 200]), np.array([255, 170, 255]))
                    meRes = self.checkPointInMap(point, np.array([10, 160, 230]), np.array([110, 255, 255]))
                    yDiff = runeRes[1][1] - meRes[1][1]
                if (direction == 1):
                    self.userObj.upStop()
                else:
                    self.userObj.downStop()
                print("start runeUse")
                # start runeUse
                time.sleep(2)
                self.getAction().send(client.Key("space"))
                time.sleep(2)
                runeUse = RuneUse(self.screen.get())
                actionArr = runeUse.use()
                print("end")
                for k in actionArr:
                    print(k.key)
                time.sleep(5)
                self.action.sendArray(actionArr)
                time.sleep(0.4)
                self.lock.release()
                thread.runeLock.release()
                self.now = int(time.time())
                # if (runeUse.success()):

