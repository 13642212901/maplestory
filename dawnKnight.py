import random

import user
import client
import time
import units

class DawnKnight(user.User):
    type = 1
    attKey = "w"
    flashTime = 0
    attTime = 2
    jumpTime = 2
    returnTime = 3
    def att(self):
        self.getAction().send(client.Key(self.attKey, random.randint(650, 700)))
        time.sleep(units.randomMs(700, 750))

    def handle(self):
        self.lock.acquire()
        if (self.groupAttTime == 3):
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
