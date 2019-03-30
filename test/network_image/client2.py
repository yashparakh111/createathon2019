import socket

s = socket.socket()
host = "10.145.56.251"
port = 12345

s.connect((host, port))
print s.recv(1024)
s.close()
