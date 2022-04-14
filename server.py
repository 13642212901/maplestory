import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 12345))
s.listen(5)
while 1:
    con, address = s.accept()
    while 1:
        msg = con.recv(1024)
        print(msg.decode('utf-8'))