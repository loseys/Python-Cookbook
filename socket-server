import socket

s = socket.socket()
s.bind(('127.0.0.1', 4444))
s.listen(5)
c, addr = s.accept()
print("Socket Up and running with a connection from", addr)
while True:
    rcvdData = c.recv(1024).decode()
    print("S:", rcvdData)
c.close()
