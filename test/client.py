import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("10.148.58.0", 1234))    # PC static IP
#s.connect((socket.gethostname(), 1234))

msg = s.recv(1024)
print(msg.decode("utf-8"))
 
