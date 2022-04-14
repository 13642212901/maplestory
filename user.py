import abc
import random
import time

import action
import client
import thread


class User(thread.ThreadController, metaclass=abc.ABCMeta):
    returnTime = 5
    direction = 1
    attTime = 1
    groupAttTime = 1
    flashKey = "f"
    flashTime = 2
    jumpTime = 2
    isJumpAtt = True
    skills = []
    type = 1
    useSkillGroupTime = 0
    userIndex = {}
    def setUserIndex(self, userIndex):
        self.userIndex = userIndex
    def __init__(self):
        thread.ThreadController.__init__(self)
        self.itemClearTime = int(time.time())
    def left(self):
        self.getAction().send(client.Key("left Down", 20))
    def leftStop(self):
        self.getAction().send(client.Key("left Up", 20))
    def right(self):
        self.getAction().send(client.Key("right Down", 20))
    def rightStop(self):
        self.getAction().send(client.Key("right Up", 20))
    def down(self):
        self.getAction().send(client.Key("down,c"))
        time.sleep(0.8)
    def downStop(self):
        pass
    def up(self):
        self.getAction().sendCombo(client.Key("up," + self.flashKey))
        time.sleep(1)
        self.getAction().send(client.Key("space"))
        time.sleep(1)
        pass
    def upStop(self):
        pass
    @abc.abstractmethod
    def att(self):
        pass
    def flash(self):
        if (self.direction == 1):
            self.getAction().sendCombo(client.Key("left," + self.flashKey))
        else:
            self.getAction().sendCombo(client.Key("right," + self.flashKey))
        time.sleep(0.15)
    def doubleJump(self, delay = 50):
        if (self.direction == 1):
            self.getAction().sendCombo(client.Key("left,c,c", delay))
        else:
            self.getAction().sendCombo(client.Key("right,c,c", delay))
    def jump(self):
        if (self.direction == 1):
            self.getAction().sendCombo(client.Key("left,c", 80))
        else:
            self.getAction().sendCombo(client.Key("right,c", 80))

    def oneMap(self):
        if (not self.flashTime == 0):
            r = random.randint(0, 20)
            ft = self.flashTime
            if (r == 1):
                ft = self.flashTime + 1
                if (not self.groupAttTime == self.returnTime):
                    self.groupAttTime = self.groupAttTime + 1
            for i in range(ft):
                self.flash()
                if (ft > 1):
                    time.sleep(0.7)

        r = random.randint(0, 20)
        at = self.attTime
        if (r == 1):
            at = at + 1
        if (self.jumpTime == 2):
            if (self.isJumpAtt):
                self.doubleJump(150)
                time.sleep(0.15)
                at = at - 1
                self.att()
                time.sleep(0.55)
            else:
                self.doubleJump(550)
                time.sleep(0.6)
        elif (self.jumpTime == 1):
            self.jump()
        for i in range(at):
            self.att()
        if (self.groupAttTime == self.returnTime):
            if (self.direction == 1):
                self.direction = 2
            else:
                self.direction = 1
            self.groupAttTime = 1
        else:
            self.groupAttTime = self.groupAttTime + 1
    def starting(self):
        thread.ThreadController.starting(self)
        self.groupAttTime = 1

    def back(self):
        self.getAction().send(client.Key("left down", 2000))
        self.getAction().send(client.Key("left up", 500))
        time.sleep(5)

    def pushSkill(self, skill):
        self.skills.append(skill)
    def getSkills(self):
        return self.skills
    def useSkill(self):
        # if (self.useSkillGroupTime == self.groupAttTime):
        #     return False
        for skill in self.skills:
            isUse = skill.use()
            if (isUse):
                self.useSkillGroupTime = self.groupAttTime
                return True
        return False
    def isItemClear(self):
        return int(time.time()) - self.itemClearTime > 120
    def pickUp(self):
        self.itemClearTime = int(time.time())
