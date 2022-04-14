import random

import user
import client
import time
import units

class Hunter(user.User):
    type = 1
    attKey = "w"
    flashTime = 0
    attTime = 1
    jumpTime = 0
    returnTime = 8
    def att(self):
        # self.getAction().send(client.Key(self.attKey, random.randint(500, 550)))
        # time.sleep(units.randomMs(500, 550))
        self.combo()
    def combo(self):
        delay = 20
        self.getAction().send(client.Key("w down", delay))
        time.sleep(0.15)

    def handle(self):
        self.lock.acquire()
        # if (self.groupAttTime == 2):
        #     if (self.direction == 2):
        #         self.down()
        d = "right"
        b = "left"
        if (self.direction == 1):
            d = "left"
            b = "right"
        if (self.groupAttTime == 1):
            print(d)
            time.sleep(0.1)
            self.getAction().send(client.Key(b + " Up", 20))
            time.sleep(0.5)
            self.getAction().send(client.Key(d + " Down", 20))
            time.sleep(1)
        if (self.type == 1):
            self.oneMap()
        self.lock.release()
        time.sleep(0.3)
    def useOneMap(self):
        self.type = 1

    def buffTpl(self):
        return ["dawnKnight/buff_top1.jpg", "dawnKnight/buff_bottom1.jpg", 150, 50]
    def flash(self):
        user.User.flash(self)
        time.sleep(units.randomMs(750, 800))
