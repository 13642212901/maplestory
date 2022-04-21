import random

import thread
import user
import client
import time
import units

class Adele(user.User):
    type = 1
    attKey = "w"
    attTime = 7
    flashTime = 0
    jumpTime = 2
    returnTime = 11
    isJumpAtt = True
    weaponSkill = []
    burningWeaponSkill = {}
    weaponTime = 0
    burningTime = 999999999999
    hasWeapon = False
    def att(self):
        isUse = False
        if (not self.groupAttTime == self.returnTime):
            isUse = self.useSkill()
        if (not isUse):
            self.getAction().send(client.Key(self.attKey, random.randint(720, 750)))
            time.sleep(units.randomMs(750, 770))
    def jumpAtt(self):
        self.getAction().send(client.Key("heroJumpAtt"))
        time.sleep(1.1)
    def pushWeaponSkill(self, s):
        self.weaponSkill.append(s)
    def setBurningWeaponSkill(self, s):
        self.burningWeaponSkill = s
    def useWeaponSkill(self):
        for skill in self.weaponSkill:
            isUse = skill.use()
            if (isUse):
                return True
        return False
    def jumpDown(self):
        self.getAction().send(client.Key("Down,c", 200))
        time.sleep(0.25)
    def jumpSkill(self):
        pass
    def highJump(self):
        self.getAction().send(client.Key("highJumpAtt"))
        time.sleep(1.25)

    def handle(self):
        self.lock.acquire()
        x = self.userIndex.getX()
        y = self.userIndex.getY()
        self.useSkill()
        print(x)
        self.jumpAtt()
        if (x > 180 ):
            self.move("Left", 50)
            self.direction = 2
            self.groupAttTime = 1
        if (x < 40):
            self.move("Right", 50)
            self.direction = 1
            self.groupAttTime = 1
        if (self.groupAttTime == self.returnTime):
            if (self.direction == 1):
                self.move("Left", 50)
                self.direction = 2
            else:
                self.move("Right", 50)
                self.direction = 1
            self.groupAttTime = 1
        else:
            self.groupAttTime = self.groupAttTime + 1

        # time.sleep(0.2)
        self.lock.release()


    def move(self, d, delay):
        self.action.send(client.Key(d + "|" + str(delay)))
        time.sleep(delay * 1.2 / 1000)
