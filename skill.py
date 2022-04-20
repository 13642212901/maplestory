import random
import threading

import thread
import client
import units
import time
import cv2

class Skill:
    cd = False
    action = {}
    useTime = 0
    def __init__(self, key, delay, cdTime):
        self.key = key
        self.cdTime = cdTime
        self.delay = delay
    def setAction(self, a):
        self.action = a
    def use(self):
        if (not self.ifCD()):
            time.sleep(0.2)
            self.action.send(client.Key(self.key, random.randint(self.delay, self.delay + 50)))
            self.useTime = int(time.time())
            self.cd = True
            time.sleep(self.delay / 1000 + 0.2)
            return True
        return False
    def ifCD(self):
        now = int(time.time())
        if (now - self.useTime >= self.cdTime):
            self.cd = False
        else:
            self.cd = True
        return self.cd
class MoveSkill(Skill):
    def use(self):
        if (not self.ifCD()):

            time.sleep(0.2)
            delay = 80
            d = "Right"
            self.action.send(client.Key(d + "|" + str(delay)))
            time.sleep(0.5)
            d = "Left"
            self.action.send(client.Key(d + "|" + str(delay)))
            time.sleep(0.5)
            self.useTime = int(time.time())
            self.cd = True
            time.sleep(self.delay / 1000 + 0.2)
            return True
        return False
class ChargingSkill(Skill):
    chargingTimes = 2
    lock = threading.Lock()
    def handle(self):
        if (self.ifCD()):
            time.sleep(self.cdTime)
            self.chargingTimes = self.chargingTimes + 1
        else:
            time.sleep(0.1)
    def ifCD(self):
        return self.chargingTimes < 2
    def use(self):
        if (not self.ifCD()):
            d = random.randint(self.delay, self.delay + 50)
            self.action.send(client.Key(self.key, d))
            self.chargingTimes = self.chargingTimes - 1
            time.sleep(d / 1000 + 0.5)
            return True
        return False

class IliumV2(Skill):
    def use(self):
        if (not self.ifCD()):
            time.sleep(1)
            self.action.send(client.Key("c," + self.key, random.randint(self.delay, self.delay + 50)))
            self.cd = True
            time.sleep(self.delay / 1000 + 0.2)
            return True
        return False
#
# class IliumCharge(Skill):
#     l = threading.Lock()
#     useTime = 0
#     def __init__(self, key, delay, tpl):
#         Skill.__init__(self, key, delay, 0)
#         self.tpl = cv2.imread(tpl)
#         self.cd = True
#     def use(self):
#         self.l.acquire()
#         if (not self.ifCD()):
#             time.sleep(0.5)
#             self.action.send(client.Key(self.key, random.randint(self.delay, self.delay + 50)))
#             self.cd = True
#             time.sleep(self.delay / 1000 + 0.3)
#             self.useTime = int(time.time())
#             self.l.release()
#             return True
#         self.l.release()
#         return False
#     def handle(self):
#         self.l.acquire()
#         cap = self.getScreen().get()
#         img = cap[1000:, 1320:]
#         gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#         ret1, thresh1 = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY)
#         res = units.match(self.tpl, thresh1, 0.01)
#         if (res[0] == True):
#             if (self.key == "r"):
#                 print(res)
#             now = int(time.time())
#             if (now - self.useTime > 10):
#                 self.cd = False
#         self.l.release()
#         time.sleep(2)
