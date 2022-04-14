import queue
import socket
import time
import queue as q

import thread as t

class Key:
    key = ""
    delay = 50
    lock = False
    def __init__(self, key, delay = 50, lock = False):
        self.key = key
        self.delay = delay
        self.lock = lock

class Client(t.ThreadController):
    def __init__(self, config):
        t.ThreadController.__init__(self)
        self.config = config
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((self.config["ip"], self.config["port"]))
        except Exception as e:
            print(e)
            exit()
        self.queue = q.Queue()

        self.s = s
    def send(self, key:Key):
        self.queue.put(key)
    def handle(self):
        k = self.queue.get()
        # print(k.key)
        s = (k.key +  "." + str(k.delay)).encode()
        res = self.s.send(s)

