import user
import client
import time
import units

class PathFinder(user.User):
    type = 1
    attKey = "w"
    flashTime = 0
    returnTime = 4
    def att(self):
        self.getAction().send(client.Key(self.attKey, units.randomMs(700, 750)))
        time.sleep(units.randomMs(500, 550))

    def handle(self):
        self.lock.acquire()
        if (self.groupAttTime == 3):
            if (self.direction == 2):
                self.down()
            self.getAction().send(client.Key("s"))
            time.sleep(0.3)
            self.getAction().send(client.Key("r"))
            time.sleep(0.8)
        if (self.type == 1):
            self.oneMap()
        self.lock.release()
        time.sleep(0.5)
    def useOneMap(self):
        self.type = 1

    def buffTpl(self):
        return ["pathfinder/buff_top1.jpg", "pathfinder/buff_bottom1.jpg", 100, 50]
