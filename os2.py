import skill
import numpy as np
import user
import time
import client
import random
import units

class Kanna(user.User):
    attKey = "w"
    skill = []
    bossTime = 0
    boss = {}
    placeSkills = []
    kishinSkill = {}
    def __init__(self):
        user.User.__init__(self)
        self.pick = Pick(self)
        self.defaultAtt = DefaultAtt(self)
    def setBoss(self, skill):
        self.boss = Boss(self, skill)
    def attCombo(self):
        self.getAction().send(client.Key("kannaAtt"))
        time.sleep(0.55)
    def att(self):
        self.getAction().send(client.Key("Ctrl", 400))
        time.sleep(0.5)

    def handle(self):
        self.lock.acquire()
        ifUse = self.boss.use()
        if (ifUse):
            self.bossTime = self.bossTime + 1
            self.boss.back()
            if (self.bossTime == 4):
                self.pick.use()
                self.defaultAtt.back()
                self.bossTime = 0
            else:
                self.defaultAtt.back()
        self.defaultAtt.run()
        # time.sleep(0.2)
        self.lock.release()
    def move(self, d, delay):
        self.action.send(client.Key(d + "|" + str(delay)))
        time.sleep(delay * 1.2 / 1000)
    def flashD(self, d):
        self.getAction().send(client.Key(d + ",f"))
        time.sleep(0.42)
    def jumpDown(self):
        self.getAction().send(client.Key("Down,c", 200))
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

class DefaultAtt():
    direction = 1
    def __init__(self, u: Kanna):
        self.u = u
    def run(self):
        self.u.useSkill()
        # print(self.u.userIndex.getX())
        self.u.attCombo()
        self.u.move("Right", 100)
        self.u.attCombo()
        self.u.flashD("Right")
        self.u.attCombo()
        self.u.flashD("Right")
        self.u.jumpExorcist()
        self.u.flashD("Left")
        self.u.attCombo()
        self.u.flashD("Left")
        time.sleep(0.35)
        self.back()
        time.sleep(0.2)


    def back(self):
        self.u.moveX(102)
        self.u.getAction().send(client.Key("Left|20"))
        time.sleep(0.1)


class Boss():
    def __init__(self, u: Kanna, s: skill.Skill):
        self.u = u
        self.s = s
    def move(self):
        time.sleep(0.2)
        self.u.attCombo()
        self.u.moveX(93)
        self.u.flashD("Up")
        self.u.move("Down", 100)
        self.u.move("Left", 30)
        time.sleep(0.1)
        self.u.attCombo()

    def use(self):
        if (not self.s.ifCD()):
            self.move()
            self.s.use()
            return True
        else:
            return False
    def back(self):
        self.u.flashD("Down")
        time.sleep(0.2)

class Pick():
    def __init__(self, u: Kanna):
        self.u = u
    def use(self):
        time.sleep(0.2)
        self.u.flashD("Right")
        time.sleep(0.7)
        self.u.flashD("Right")
        self.u.usePlaceSkill()
        self.u.flashD("Right")
        self.u.attCombo()
        time.sleep(0.1)
        self.u.flashD("Up")
        self.u.attCombo()
        time.sleep(0.5)
        self.u.Exorcist()
        time.sleep(0.2)

        self.u.flashD("Left")
        self.u.attCombo()
        time.sleep(0.1)
        self.u.flashD("Down")
        self.u.attCombo()

        self.u.flashD("Left")
        self.u.attCombo()
        time.sleep(0.1)
        self.u.flashD("Left")
        self.u.attCombo()
        self.u.flashD("Left")
        self.u.attCombo()
        time.sleep(0.1)
        self.u.flashD("Left")
        self.u.attCombo()
        self.u.flashD("Left")
        self.u.attCombo()
        time.sleep(0.1)
        self.u.moveX(38)
        self.u.useKishin()
        self.u.move("Right", 20)
        time.sleep(0.1)
        self.u.flashD("Right")
        self.u.attCombo()
        time.sleep(0.1)
        self.u.flashD("Up")
        self.u.attCombo()
        self.u.move("Left", 150)
        self.u.flashD("Up")
        self.u.attCombo()
        time.sleep(0.1)
        self.u.flashD("Down")
        self.u.attCombo()
        self.u.flashD("Down")
        self.u.attCombo()
        time.sleep(0.1)
        self.u.flashD("Right")
        self.u.attCombo()
        self.u.flashD("Right")
        self.u.attCombo()



