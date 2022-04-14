# import Socket  # 导入 socket 模块
import socket
import PyHook3 as pyHook
import pythoncom

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conRet = s.connect(('127.0.0.1', 12345))
print(conRet)
def switch(event) :
    if (event.Key == 'T') :
        print('123')
        ret = s.send(('111').encode())
        print(ret)
    if (event.Key == 'Y') :
        close = True
        exit(0)
    return True
hm = pyHook.HookManager()
hm.KeyDown = switch
hm.HookKeyboard()
pythoncom.PumpMessages()