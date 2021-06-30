import socket

s = socket.socket()
s.connect(('127.0.0.1', 4444))
while True:
    str = input("String: ")
    s.send(str.encode());
s.close()
