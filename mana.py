import time

import client
import thread


class Mana(thread.ThreadController):
    def handle(self):
        cap = self.getScreen().get()
        res = cap[1050, 920]
        if (res[0] > 99 and res[0] < 110 and res[1] > 93 and res[1] < 110 and res[2] >95 and res[2] < 110):
            self.getAction().send(client.Key("alt"))

        time.sleep(0.5)
