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
import hoyoung
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

user = hoyoung.Hoyoung()
food = skill.Skill("9", 450, 250)
totem = skill.Skill("f10", 1500, 115)
sage = skill.Skill("5", 450, 94)
star = skill.Skill("2", 450, 43)
stone = skill.Skill("g", 450, 6)
gold = skill.Skill("d", 450, 11)
consuming = skill.Skill("Shift", 450, 8)
ghost = skill.Skill("x", 450, 46)
clone = skill.Skill("z", 450, 0)
tiger = skill.Skill("e", 450, 190)
ton = skill.Skill("a", 450, 1)
wrath = skill.Skill("s", 500, 190)
rampage = skill.Skill("t", 500, 190)
three = skill.Skill("v", 500, 95)
butterfly = skill.Skill("3", 450, 95)
warp = skill.Skill("4", 450, 100)
user.setStone(stone)
user.setGold(gold)
user.setConsuming(consuming)
user.setGhost(ghost)
user.setClone(clone)
user.setTiger(tiger)
user.setTon(ton)
user.setThree(three)
user.setWrath(wrath)
user.setRampage(rampage)
user.setButterFly(butterfly)
user.setWarp(warp)

user.setSage(sage)
user.setStar(star)
# user.pushSkill(food)
userIndex = map.UserIndex()
user.setUserIndex(userIndex)
user.pushSkill(totem)
application = app.App({"socket": {"port": 12345, "ip": "127.0.0.1"}}, user)
application.pushSkill(sage)
application.pushSkill(star)
application.pushSkill(food)
application.pushSkill(totem)
application.pushSkill(stone)
application.pushSkill(gold)
application.pushSkill(consuming)
application.pushSkill(ghost)
application.pushSkill(clone)
application.pushSkill(tiger)
application.pushSkill(ton)
application.pushSkill(three)
application.pushSkill(wrath)
application.pushSkill(rampage)
application.pushSkill(butterfly)
application.pushSkill(warp)
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
