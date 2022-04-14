import client
import client as c
import action as a
import danger
import screen as s
import rune
import user

class App:
    isStart = 0
    skills = []
    def __init__(self, config, userObj):
        self.config = config
        self.threads = []
        self.userObj = userObj
    def run(self):
        self.clientObj = c.Client(self.config["socket"])
        self.action = a.Action(self.clientObj)
        for skill in self.skills:
            skill.setAction(self.action)
        self.screen = s.Screen()
        self.pushThread(self.clientObj)
        self.pushThread(self.screen)
        self.userObj.setAction(self.action)
        self.pushThread(rune.RuneCheck(self.userObj))
        self.pushThread(self.userObj)
        # self.pushThread(danger.Danger())
        for thread in self.threads:
            print(thread)
            thread.setAction(self.action)
            thread.setScreen(self.screen)
            thread.start()
            thread.init()
    def pushSkill(self, s):
        self.skills.append(s)

    def pushThread(self, thread):
        self.threads.append(thread)
    def open(self):
        if (self.isStart == 0):
            for thread in self.threads:
                thread.starting()
            self.isStart = 1
            print("start")
        else:
            for thread in self.threads:
                thread.stoping()
            self.isStart = 0
            print("stop")
    def close(self):
        for thread in self.threads:
            thread.close()
        self.action.send(client.Key("stop"))
    def getUser(self):
        return self.userObj