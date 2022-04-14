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

user = ilium.Ilium()
box = skill.ChargingSkill("Alt", 400, 21)
v2 = skill.IliumV2("2", 1500, 181)
v4 = skill.Skill("g", 500, 181)
q = skill.IliumCharge("q", 500, "ilium/q.jpg")
w = skill.IliumCharge("w", 200, "ilium/w.jpg")
e = skill.IliumCharge("e", 400, "ilium/e.jpg")
r = skill.IliumCharge("r", 300, "ilium/r.jpg")
warrior = skill.Skill("7", 500, 900)
totem = skill.Skill("h", 300, 115)
s = skill.Skill("s", 300, 121)
food = skill.Skill("9", 500, 250)
s8 = skill.Skill("8", 500, 181)
user.setBoxSkill(box)
user.setWingSkill(r)
user.pushSkill(warrior)
user.pushSkill(food)
user.pushSkill(totem)
# user.pushSkill(s)
user.pushSkill(v2)
# user.pushSkill(s8)
user.pushSkill(v4)
user.pushSkill(q)
# user.pushSkill(w)
# user.pushSkill(e)
userIndex = map.UserIndex()
user.setUserIndex(userIndex)
application = app.App({"socket": {"port": 12345, "ip": "127.0.0.1"}}, user)
application.pushThread(box)
application.pushThread(warrior)
application.pushThread(totem)
application.pushThread(food)
application.pushThread(s)
application.pushThread(v2)
application.pushThread(v4)
application.pushThread(s8)
application.pushThread(q)
application.pushThread(w)
application.pushThread(e)
application.pushThread(r)

# buffTpl = user.buffTpl()
# buff = Buff.Buff().setting(client.Key("5", 1800), buffTpl[0], buffTpl[1], buffTpl[2], buffTpl[3])

chance = Buff.Chance()
Eat = Buff.Eat()
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
