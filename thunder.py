import random

import user
import client
import time
import units

class Thunder(user.User):
    type = 1
    attKey = "w"
    flashTime = 0
    attTime = 1
    jumpTime = 0
    returnTime = 5
    def att(self):
        # self.getAction().send(client.Key(self.attKey, random.randint(500, 550)))
        # time.sleep(units.randomMs(500, 550))
        self.combo()
    def combo(self):
        delay = 20
        if (self.groupAttTime == self.returnTime):
            delay = 800
        self.getAction().send(client.Key("combo1", delay))
        time.sleep(0.65)

    def handle(self):
        self.lock.acquire()
        # if (self.groupAttTime == 2):
        #     if (self.direction == 2):
        #         self.down()
        if (self.type == 1):
            self.oneMap()
        if (self.groupAttTime == 1):
            time.sleep(1)
            d = "right"
            if (self.direction == 1):
                d = "left"
                self.getAction().send(client.Key("r", 1100))
                time.sleep(1.1)
            print(d)
            self.getAction().send(client.Key(d + "|100"))
            time.sleep(0.9)
            self.down()
        self.lock.release()
        time.sleep(0.5)
    def useOneMap(self):
        self.type = 1

    def buffTpl(self):
        return ["dawnKnight/buff_top1.jpg", "dawnKnight/buff_bottom1.jpg", 150, 50]
    def flash(self):
        user.User.flash(self)
        time.sleep(units.randomMs(750, 800))
