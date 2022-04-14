import random

import thread
import user
import client
import time
import units
import numpy as np

class Hoyoung(user.User):
    type = 1
    attKey = "r"
    attTime = 7
    flashTime = 0
    jumpTime = 2
    returnTime = 9
    isJumpAtt = True
    burningWeaponSkill = {}
    weaponTime = 0
    burningTime = 999999999999
    hasWeapon = False
    starMode = {}
    star = {}
    sage = {}
    stone = {}
    gold = {}
    consuming = {}
    ghost = {}
    clone = {}
    tiger = {}
    ton = {}
    wrath = {}
    three = {}
    butterfly = {}
    warp = {}
    attBuffUseTime = 0
    def __init__(self):
        user.User.__init__(self)
        self.starMode = StarMode(self)
    def att(self):
        self.getAction().send(client.Key(self.attKey, random.randint(900, 950)))
        time.sleep(units.randomMs(950, 970))
    def jumpAtt(self):
        self.getAction().send(client.Key("heroJumpAtt"))
        time.sleep(0.9)
    def jumpDown(self):
        self.getAction().send(client.Key("Down,c", 200))
        time.sleep(0.25)
    def jumpSkill(self):
        pass
    def highJump(self):
        self.getAction().send(client.Key("highJumpAtt"))
        time.sleep(1.25)

    def setWrath(self, s):
        self.wrath = s
    def useWrath(self):
        return self.wrath.use()
    def setButterFly(self, s):
        self.butterfly = s
    def useButterFly(self):
        return self.butterfly.use()
    def setWarp(self, s):
        self.warp = s
    def useWarp(self):
        return self.warp.use()
    def setThree(self, s):
        self.three = s
    def useThree(self):
        return self.three.use()
    def setTon(self, s):
        self.Ton = s
    def useTon(self):
        return self.Ton.use()
    def setClone(self, s):
        self.clone = s
    def useClone(self):
        return self.clone.use()
    def setTiger(self, s):
        self.tiger = s
    def useTiger(self):
        return self.tiger.use()
    def setStar(self, s):
        self.star = s
    def useStar(self):
        return self.star.use()
    def setSage(self, s):
        self.sage= s
    def useSage(self):
        return self.sage.use()
    def setStone(self, s):
        self.stone = s
    def useStone(self):
        return self.stone.use()
    def setGold(self, s):
        self.gold = s
    def useGold(self):
        return self.gold.use()
    def setConsuming(self, s):
        self.consuming = s
    def useConsuming(self):
        return self.consuming.use()
    def setGhost(self, s):
        self.ghost = s
    def useGhost(self):
        return self.ghost.use()
    def fly(self):
        self.getAction().send(client.Key("fly", 200))
        time.sleep(0.25)
    def flyStop(self):
        self.getAction().send(client.Key("flyStop", 50))
    def move(self, d, delay):
        self.action.send(client.Key(d + "|" + str(delay)))
        time.sleep(delay * 1.2 / 1000)
    def jump(self):
        self.getAction().sendCombo(client.Key("c", 50))
        time.sleep(0.05)
    def tripleJump(self, delay = 50):
        self.getAction().sendCombo(client.Key("tripleJump", delay))
        time.sleep(delay * 1.2 / 1000)

    def moveX(self, X):
        x = self.userIndex.getX()
        backX = X
        diff = np.abs(x - backX)
        # print(x, diff)
        t = diff * 55
        if (t > 2000 or t == 0):
            return
        if (x > backX):
            dStr = "Left"
            self.getAction().send(client.Key(dStr + "|" + str(t)))
        elif (x < backX):
            dStr = "Right"
            self.getAction().send(client.Key(dStr + "|" + str(t)))
        time.sleep(t / 1000 + 0.3)
        time.sleep(0.2)
        x = self.userIndex.getX()
        if (np.abs(x - X) > 1):
            self.moveX(X)

    def useAttBuff(self):
        if (int(time.time()) - self.attBuffUseTime > 30):
            isUse = self.useWarp()
            if (not isUse):
                self.useThree()

    def handle(self):
        self.lock.acquire()
        x = self.userIndex.getX()
        y = self.userIndex.getY()
        isRun = self.starMode.run()
        if (isRun):
            self.starMode.back()
            self.moveX(90)
            self.move("Right", 20)
        self.useSkill()
        if (self.useGold()):
            time.sleep(0.1)
        self.att()
        # time.sleep(0.2)
        self.lock.release()

class StarMode:
    u = {}
    def __init__(self, u:Hoyoung):
        self.u = u
    def go(self):
        time.sleep(0.1)
        self.u.move("Left", 30)
        time.sleep(0.1)
        self.u.tripleJump()
        time.sleep(2)
        self.u.moveX(44)
        print(self.u.userIndex.getY())
        print(self.u.userIndex.getX())
        if (self.u.userIndex.getY() < 83):
            self.u.jumpDown()
            time.sleep(0.1)
        if (self.u.userIndex.getY() < 83):
            self.u.jumpDown()
            time.sleep(0.1)
        if (self.u.userIndex.getY() > 83):
            self.u.att()
            time.sleep(0.1)

    def run(self):
        if (not self.u.star.ifCD()):
            self.go()
            isUse = self.u.useSage()
            time.sleep(0.3)
            self.u.useGhost()
            time.sleep(0.65)
            self.u.useStar()
            time.sleep(0.3)
            if (isUse):
                time.sleep(0.25)
                self.u.useClone()
                time.sleep(0.4)
                self.u.useButterFly()
                time.sleep(0.1)
            return True
        else:
            return False
    def back(self):
        self.u.move("Right", 30)
        time.sleep(0.1)
        self.u.tripleJump()
        time.sleep(1.5)
