# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from datetime import time
import time as t
import PyHook3 as pyHook
import pythoncom

import Buff
import app
import client
import os

import dawnKnight
import hero
import hunter
import ilium
import kanna
import luminous



# c = client.Client({"port": 12345, "ip": "127.0.0.1"})
# c.starting()
# c.start()
import mana
import map
import pahtfinder
import shade
import skill
import thunder


def switch(event) :
    if (event.Key == 'U') :
        application.open()
        # c.send(client.Key("left,f"))
        # u = application.getUser()
        # application.clientObj.starting()
        # u.att()
        # u.att()
        # u.att()
    if (event.Key == 'Y') :
        application.close()
        print("eixt")
        os._exit(0)
    return True

# user = luminous.Luminous()
# user = pahtfinder.PathFinder()
# user = shade.Shade()
# user = thunder.Thunder()
# user = hunter.Hunter()

# hero
# user = hero.Hero()
# shout = skill.Skill("s", 1200, 10)
# puncture = skill.Skill("d", 1000, 5)
# rising = skill.Skill("a", 1000, 10)
# user.pushSkill(shout)
# user.pushSkill(puncture)
# user.pushSkill(rising)
# application = app.App({"socket": {"port": 12345, "ip": "127.0.0.1"}}, user)
# application.pushThread(shout)
# application.pushThread(puncture)
# application.pushThread(rising)

user = kanna.Kanna()
totem = skill.Skill("m", 300, 115)
food = skill.Skill("3", 300, 250)
white = skill.Skill("6", 300, 500)
domain = skill.Skill("x", 300, 216)
kishin = skill.Skill("s", 300, 60)
v4 = skill.Skill("t", 900, 180)
boss = skill.Skill("r", 400, 29)
warrior = skill.Skill("5", 500, 900)
tengu = skill.Skill("z", 50, 0.5)
s8 = skill.Skill("8", 500, 180)

user.setBoss(boss)
user.setTengu(tengu)
user.setKishinSkill(kishin)
user.pushSkill(s8)
# user.pushSkill(totem)
userIndex = map.UserIndex()
user.setUserIndex(userIndex)
application = app.App({"socket": {"port": 12345, "ip": "127.0.0.1"}}, user)
application.pushSkill(s8)
# buffTpl = user.buffTpl()
# buff = Buff.Buff().setting(client.Key("5", 1800), buffTpl[0], buffTpl[1], buffTpl[2], buffTpl[3])

# application.pushThread(buff)
# application.pushThread(chance)
# application.pushThread(mana.Mana())
# application.pushThread(Buff.Default())
# application.pushThread(Buff.Warrior())
# application.pushThread(Eat)
application.pushThread(userIndex)
application.run()

hm = pyHook.HookManager()
hm.KeyDown = switch
hm.HookKeyboard()
pythoncom.PumpMessages()
