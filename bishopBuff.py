import skill
import numpy as np
import user
import time
import client
import random
import units

class BishopBuff(user.User):
    attKey = "w"
    skill = []
    bossTime = 0
    boss = {}
    placeSkills = []
    kishinSkill = {}
    tenguSkill = {}
    def __init__(self):
        user.User.__init__(self)
    def attCombo(self):
        self.getAction().send(client.Key("kannaAtt"))
        time.sleep(0.55)
    def att(self):
        self.getAction().send(client.Key("Ctrl", 400))
        time.sleep(0.5)

    def handle(self):
        self.lock.acquire()
        isUse = self.useSkill()
        print(self.userIndex.getX())
        if (isUse):
            time.sleep(0.5)
            self.moveX(104)
        if (self.direction == 1):
            self.direction = 2
            # self.move("Left", 50)
        else:
            self.direction = 1
            # self.move("Right", 50)
        time.sleep(0.5)
        # time.sleep(0.2)
        self.lock.release()
    def go(self):
        self.flashD("Up")
        time.sleep(0.3)
        # self.flashD("Down")
        # time.sleep(0.3)
    def back(self):
        self.flashD("Down")
        time.sleep(0.3)
        # self.flashD("Up")
        # time.sleep(0.3)


    def move(self, d, delay):
        self.action.send(client.Key(d + "|" + str(delay)))
        time.sleep(delay * 1.2 / 1000)
    def flashD(self, d):
        self.getAction().send(client.Key(d + ",f"))
        time.sleep(0.42)
    def jumpDown(self):
        self.getAction().send(client.Key("Down,c,c", 200))
        time.sleep(0.25)
    def jumpExorcist(self):
        self.getAction().send(client.Key("jumpExorcist", 900))
        time.sleep(1)
    def Exorcist(self):
        self.getAction().send(client.Key("q", 800))
        time.sleep(0.9)
    def pushPlaceSkill(self, s):
        self.placeSkills.append(s)
    def setKishinSkill(self, s):
        self.kishinSkill = s
    def useKishin(self):
        return self.kishinSkill.use()
    def usePlaceSkill(self):
        # if (self.useSkillGroupTime == self.groupAttTime):
        #     return False
        for skill in self.placeSkills:
            isUse = skill.use()
            if (isUse):
                self.useSkillGroupTime = self.groupAttTime
                return True
        return False
    def moveX(self, X):
        x = self.userIndex.getX()
        backX = X
        diff = np.abs(x - backX)
        # print(x, diff)
        t = diff * 75
        if (x > backX):
            dStr = "Left"
            self.getAction().send(client.Key(dStr + "|" + str(t)))
        elif (x < backX):
            dStr = "Right"
            self.getAction().send(client.Key(dStr + "|" + str(t)))
        time.sleep(t / 1000 + 0.3)
    def useTengu(self):
        self.tenguSkill.use()
        time.sleep(0.05)
    def setTengu(self, s):
        self.tenguSkill = s
    def checkX(self, x1, y1):
        x = self.userIndex.getX()
        y = self.userIndex.getY()
        i = 0
        while x < x1 - 3 or x > x1 + 3 or y > y1 + 3 or y < y1 - 3:
            y = self.userIndex.getY()
            x = self.userIndex.getX()
            if (i > 11):
                print(x, y)
                self.attCombo()
                time.sleep(0.1)
                self.jumpDown()
                i = 0
            i = i + 1
            time.sleep(0.1)
