#!/usr/bin/python3
import random
import threading
import abc
import time

threadLock = threading.Lock()
runeLock = threading.Lock()

class ThreadController(threading.Thread, metaclass=abc.ABCMeta):
    action = {}
    screen = {}
    isRun = True
    def __init__(self):
        threading.Thread.__init__(self)
        self.lock = threadLock
        self.isStart = 0
    def setAction(self, action):
        self.action = action
    def setScreen(self, screen):
        self.screen = screen
    def getAction(self):
        return self.action
    def getScreen(self):
        return self.screen
    def run(self):
        while self.isRun:
            if (self.isStart == 1):
                self.handle()
            time.sleep(0.05)
            pass
    @abc.abstractmethod
    def handle(self):
        pass
    def starting(self):
        self.isStart = 1
    def init(self):
        pass
    def stoping(self):
        self.isStart = 0
    def close(self):
        self.isRun = False

