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
        self.wrath.use()
    def setButterFly(self, s):
        self.butterfly = s
    def useButterFly(self):
        self.butterfly.use()
    def setWarp(self, s):
        self.warp = s
    def useWarp(self):
        self.warp.use()
    def setThree(self, s):
        self.three = s
    def useThree(self):
        self.three.use()
    def setTon(self, s):
        self.Ton = s
    def useTon(self):
        self.Ton.use()
    def setClone(self, s):
        self.clone = s
    def useClone(self):
        self.clone.use()
    def setTiger(self, s):
        self.tiger = s
    def useTiger(self):
        self.tiger.use()
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
        self.ghost.use()
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
    def moveX(self, X):
        x = self.userIndex.getX()
        backX = X
        diff = np.abs(x - backX)
        # print(x, diff)
        t = diff * 40
        if (t > 2000 or t == 0):
            return
        if (x > backX):
            dStr = "Left"
            self.getAction().send(client.Key(dStr + "|" + str(t)))
        elif (x < backX):
            dStr = "Right"
            self.getAction().send(client.Key(dStr + "|" + str(t)))
        time.sleep(t / 1000 + 0.3)

    def handle(self):
        self.lock.acquire()
        x = self.userIndex.getX()
        self.moveX(79)
        self.useSkill()
        isRun = self.starMode.run()
        if (isRun):
            self.starMode.back()
        else:
            if (not self.stone.ifCD()):
                self.move("Right", 25)
                time.sleep(0.2)
                self.stone.use()
                time.sleep(0.5)
                self.move("Left", 25)
                time.sleep(0.1)
            else:
                if (not self.gold.ifCD()):
                    self.move("Right", 25)
                    time.sleep(0.2)
                    self.jump()
                    self.gold.use()
                    time.sleep(0.5)
                    self.move("Left", 25)
                    time.sleep(0.1)
                else:
                    if (not self.consuming.ifCD()):
                        self.move("Right", 25)
                        time.sleep(0.2)
                        self.jump()
                        self.consuming.use()
                        time.sleep(0.5)
                        self.move("Left", 25)
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
        self.u.fly()
        self.u.move("Right", 150)
        time.sleep(0.15)
        self.u.move("Up", 1250)
        self.u.flyStop()
        time.sleep(0.5)
        y = self.u.userIndex.getY()
        if (y == 103):
            self.u.fly()
            self.u.move("Right", 80)
            time.sleep(0.15)
            self.u.move("Up", 400)
            self.u.flyStop()
            time.sleep(0.4)
        y = self.u.userIndex.getY()
        if (y > 87):
            self.u.move("Up", 300)
            time.sleep(0.2)
        if (y < 87):
            self.u.jumpDown()
            time.sleep(0.5)

    def run(self):
        if (not self.u.star.ifCD()):
            self.go()
            isUse = self.u.useSage()
            time.sleep(0.3)
            self.u.useGhost()
            time.sleep(0.55)
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
        self.u.fly()
        self.u.move("Left", 140)
        time.sleep(0.15)
        self.u.move("Down", 800)
        self.u.flyStop()
        time.sleep(0.5)
