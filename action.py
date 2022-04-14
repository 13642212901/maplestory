import random
import time
import client as c

class Action:
    def __init__(self, client:c.Client):
        self.client = client
    def sendArray(self, arr):
        for k in arr:
            self.client.send(k)
            number = random.randrange(20, 50)
            time.sleep(number / 100)
    def send(self, key):
        self.client.send(key)
    def sendCombo(self, key):
        self.client.send(key)
