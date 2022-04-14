import random

import numpy as np

import thread
import user
import client
import time
import units

class Ilium(user.User):
    type = 1
    # 1 左 2 右 3 上 4 下 13 左上 14 左下 23 右上 24 右下
    direction = 1
    mode = 1
    wingSkill = {}
    def __init__(self):
        user.User.__init__(self)
        self.routine = IliumRoutine(self)
        self.fly = IliumFly(self, self.routine)
        self.iClient = client.Client({"ip": "127.0.0.1", "port": 12346})
    def setBoxSkill(self, skill):
        self.routine.setBoxSkill(skill)
    def setWingSkill(self, skill):
        self.wingSkill = skill
    def att(self):
        self.getAction().send(client.Key("iliumnAtt"))
        time.sleep(1.3)

    def handle(self):
        self.lock.acquire()
        if (not self.wingSkill.ifCD()):
            if (self.direction == 2):
                self.mode = 2
        if (self.mode == 1):
            self.routine.run()
        else:
            print("fly")
            self.fly.run()
            self.routine.back()
            self.mode = 1
        self.lock.release()

    def useOneMap(self):
        self.type = 1

    def buffTpl(self):
        return ["pathfinder/buff_top1.jpg", "pathfinder/buff_bottom1.jpg", 100, 50]
    def up(self):
        self.getAction().send(client.Key("shift", random.randint(720, 750)))
        time.sleep(3)
    def box(self, delay = 50, follow = False):
        r = random.randint(50, 100)
        if (follow):
            self.getAction().send(client.Key("Up,Shift", r))
        else:
            self.getAction().send(client.Key("Shift", r))
        time.sleep(0.4)
        pass
    def left(self):
        self.getAction().sendCombo(client.Key("left,ctrl", 100))
        time.sleep(0.25)
    def right(self):
        self.getAction().sendCombo(client.Key("right,ctrl", 100))
        time.sleep(0.25)
    def flash(self):
        if (self.direction == 1):
            self.getAction().sendCombo(client.Key("left," + self.flashKey + ",Ctrl", 400))
        else:
            self.getAction().sendCombo(client.Key("right," + self.flashKey + ",Ctrl", 400))
        time.sleep(0.7)


class IliumRoutine:
    flashTimes = 0
    # 1 左 2 右 3 上 4 下 13 左上 14 左下 23 右上 24 右下
    direction = 1
    attTimes = 4
    boxSkill = {}
    # 1 攻击前 2 其他 3 瞬移后前面 4 瞬移后原地 5 一边真一边假
    boxSkillMode = 6
    boxDirection = [1, 2]
    boxMode5Direction = 1
    boxTime = 0
    isBoxMove = True
    groupTimes = 1
    def __init__(self, u):
        self.u = u
    def att(self):
        self.u.att()
    def run(self):
        self.u.useSkill()
        self.u.useSkillGroupTime = 2
        r = random.randint(0, 20)
        at = self.attTimes
        if (r == 1):
            at = at + 1
        if (self.boxSkillMode == 1):
            if (not self.boxSkill.ifCD()):
                self.u.box(250 * (self.flashTimes + 1))
                self.boxSkill.use()
                self.isBoxMove = False
        else:
            # if (self.isBoxMove and self.direction == 1):
            # if (self.direction == 1):
            self.isBoxMove = False
            # self.u.box()
        if (self.boxSkillMode == 6):
            if (not self.boxSkill.ifCD()):
                time.sleep(0.8)
                if (self.groupTimes > 2):
                    if (self.u.userIndex.getX() < 88):
                        self.u.getAction().send(client.Key("Right|150"))
                        time.sleep(0.5)
                        self.u.getAction().send(client.Key("Left|100"))
                        time.sleep(0.3)
                    else:
                        self.u.getAction().send(client.Key("Right|100"))
                        time.sleep(0.5)
                        self.u.getAction().send(client.Key("Left|150"))
                    time.sleep(0.3)
                    self.groupTimes = 1
                self.u.box(250, True)
                time.sleep(0.3)
                self.boxSkill.use()
                time.sleep(0.3)
                self.u.box(250)
                self.isBoxMove = False
        # at = at - 1
        for i in range(at):
            self.att()
            # self.u.getAction().send(client.Key("Ctrl", 600))
            # time.sleep(0.62)
        boxReturn = False
        if (self.boxSkillMode == 5 and self.direction in self.boxDirection and self.direction == self.boxMode5Direction):
            if (not self.boxSkill.ifCD()):
                time.sleep(0.25)
                self.boxSkill.use()
                boxReturn = True
                time.sleep(0.15)
                if (self.boxMode5Direction == 1):
                    self.boxMode5Direction = 2
                else:
                    self.boxMode5Direction = 1
        ft = self.flashTimes
        for i in range(ft):
            print(self.u.userIndex.getX())
            if ((self.direction == 1 and self.u.userIndex.getX() > 99) or (self.direction == 2 and self.u.userIndex.getX() < 101 and not self.u.userIndex.getX() == 105)):
                self.u.flash()
        if (self.boxSkillMode in [3, 4] and self.direction in self.boxDirection):
            # if (int(time.time()) - self.boxTime > 20):
            self.isBoxMove = True
            self.boxTime = int(time.time())
            if (self.boxSkillMode == 3):
                self.u.box()
                time.sleep(0.7)
            time.sleep(0.3)
            self.boxSkill.use()
            time.sleep(0.15)
        print("b", self.u.userIndex.getX())
        # if (self.direction == 1 and self.u.userIndex.getX() > 75):
        #     self.u.getAction().send(client.Key("Left|200"))
        #     time.sleep(0.3)
        # if (self.direction == 2 and self.u.userIndex.getX() < 118):
        #     self.u.getAction().send(client.Key("Right|200"))
        #     time.sleep(0.3)
        if (self.boxSkillMode == 5 and self.direction in self.boxDirection and boxReturn):
            self.u.box()
            time.sleep(0.2)
        if (self.direction == 1):
            # self.u.left()
            self.direction = 2
            self.u.direction = self.direction
        elif (self.direction == 2):
            # self.u.right()
            self.direction = 1
            self.u.direction = self.direction
        self.groupTimes = self.groupTimes + 1
    def setBoxSkill(self, skill):
        self.boxSkill = skill
    def getDirection(self):
        return self.direction
    def back(self):
        x = self.u.userIndex.getX()
        self.direction = 1
        self.u.direction = self.direction
        diff = np.abs(x - 90)
        t = diff * 73
        if (x > 105):
            dStr = "Left"
            self.u.getAction().send(client.Key(dStr + "|" + str(t)))
        elif (x < 105):
            dStr = "Right"
            self.u.getAction().send(client.Key(dStr + "|" + str(t)))
        time.sleep(t / 1000 + 0.2)
        self.u.left()
        time.sleep(1)
        self.groupTimes = 1


class IliumFly:
    # 1 左 2 右 3 上 4 下 13 左上 14 左下 23 右上 24 右下
    direction = 1
    directionMap = {1: "Left", 2: "Right", 3: "Up", 4: "Down"}
    vortexUsed = False
    # directions = [{"d": 2, "t": 150}, {"d": 3, "t": 141}, {"d": 2, "t": 1100}, {"d": 1, "t": 30}, {"d": 4, "t": 780}, {"d": 5, "t": 1000}, {"d": 4, "t": 80}, {"d": 3, "t": 180}, {"d": 5, "t": 600}, {"d": 1, "t": 2200}, {"d": 3, "t": 720}, {"d": 4, "t": 200}, {"d": 5, "t": 200}, {"d": 1, "t": 800}, {"d": 2, "t": 30}, {"d": 4, "t": 750}, {"d": 2, "t": 1300}, {"d": 5, "t": 700}, {"d": 3, "t": 600}]
    # directions = [{"d": 2, "t": 1300}, {"d": 3, "t": 140}, {"d": 4, "t": 150}, {"d": 1, "t": 3100}, {"d": 3, "t": 140}, {"d": 4, "t": 150}, {"d": 2, "t": 1500}, {"d": 1, "t": 1400}, {"d": 4, "t": 850}, {"d": 2, "t": 800}, {"d": 3, "t": 280}, {"d": 2, "t": 1500}, {"d": 2, "t": 250}, {"d": 3, "t": 150}, {"d": 1, "t": 80}, {"d": 5, "t": 1500}, {"d": 1, "t": 1200}]
    directions = [{"d": 1, "t": 550}, {"d": 3, "t": 140}, {"d": 4, "t": 150}, {"d": 2, "t": 1900}, {"d": 1, "t": 20}, {"d": 5, "t": 520}, {"d": 4, "t": 350}, {"d": 1, "t": 2000}, {"d": 2, "t": 20}, {"d": 5, "t": 320}, {"d": 4, "t": 320}, {"d": 2, "t": 1700}, {"d": 1, "t": 20}, {"d": 5, "t": 600}, {"d": 1, "t": 650}, {"d": 3, "t": 500}, {"d": 5, "t": 400}]
    lastMoveTimes = 5
    def __init__(self, u, r):
        self.u = u
        self.r = r

    def run(self):
        self.u.wingSkill.use()
        self.u.iClient.send(client.Key("Ctrl"))
        self.u.iClient.handle()
        time.sleep(0.25)
        for i in range(len(self.directions)):
            d = self.directions[i]["d"]
            t = int(self.directions[i]["t"])
            if (d == 5):
                time.sleep(t / 1000)
                continue
            if (self.r.direction == 2):
                if (d == 1):
                    d = 2
                elif (d == 2):
                    d = 1
            dStr = self.directionMap[d]
            self.u.getAction().send(client.Key(dStr + "|" + str(t)))
            dy = 0.15
            if (t > 500):
                dy = 0.2
            if (t > 1000):
                dy = 0.3
            time.sleep(t/1000 + dy)

        self.u.getAction().send(client.Key("t", 50))
        time.sleep(0.2)
        self.u.getAction().send(client.Key("t", 50))
        time.sleep(0.2)
        self.u.getAction().send(client.Key("t", 1000))
        time.sleep(1)
        for i in range(self.lastMoveTimes):
            self.u.getAction().send(client.Key("Right|100"))
            time.sleep(0.8)
            self.u.getAction().send(client.Key("Left|100"))
            time.sleep(0.8)



class IliumFlyAtt(thread.ThreadController):
    def att(self):
        self.getAction().send(client.Key("Ctrl", 350))
        time.sleep(0.5)
    def handle(self):
        self.att()