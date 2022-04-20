import random

import thread
import user
import client
import time
import units

class slayer(user.User):
    type = 1
    attKey = "w"
    attTime = 7
    flashTime = 0
    jumpTime = 2
    returnTime = 7
    isJumpAtt = True
    weaponSkill = []
    burningWeaponSkill = {}
    weaponTime = 0
    burningTime = 999999999999
    hasWeapon = False
    groupAttTime = 0
    def att(self):
        self.getAction().send(client.Key("aaaAtt"))
        time.sleep(1)
    def fly(self, d):
        self.getAction().send(client.Key("fly" + d))
        time.sleep(0.8)

    def jumpAtt(self):
        self.getAction().send(client.Key("heroJumpAtt"))
        time.sleep(0.9)
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
        self.att()
        if (self.direction == 1):
            self.fly("Left")
        else:
            self.fly("Right")
        print(self.groupAttTime)
        if (self.returnTime == self.groupAttTime):
            self.groupAttTime = 0
            if (self.direction == 1):
                self.direction = 2
            else:
                self.direction = 1
        else:
            self.groupAttTime = self.groupAttTime + 1
        # time.sleep(0.2)
        self.lock.release()


    def move(self, d, delay):
        self.action.send(client.Key(d + "|" + str(delay)))
        time.sleep(delay * 1.2 / 1000)
