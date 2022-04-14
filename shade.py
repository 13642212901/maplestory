import random

import user
import client
import time
import units

class Shade(user.User):
    type = 1
    attKey = "w"
    flashTime = 0
    attTime = 2
    jumpTime = 2
    returnTime = 4
    def att(self):
        # self.getAction().send(client.Key("e", random.randint(850, 900)))
        # time.sleep(units.randomMs(800, 850))
        # self.getAction().send(client.Key("r", random.randint(850, 900)))
        # time.sleep(units.randomMs(800, 850))
        self.getAction().send(client.Key(self.attKey, random.randint(1050, 1150)))
        time.sleep(units.randomMs(1050, 1150))

    def handle(self):
        self.lock.acquire()
        if (self.groupAttTime == 2):
            if (self.direction == 2):
                self.down()
        if (self.type == 1):
            self.oneMap()
        self.lock.release()
        time.sleep(0.5)
    def useOneMap(self):
        self.type = 1

    def buffTpl(self):
        return ["dawnKnight/buff_top1.jpg", "dawnKnight/buff_bottom1.jpg", 150, 50]
    def flash(self):
        user.User.flash(self)
        time.sleep(units.randomMs(750, 800))
