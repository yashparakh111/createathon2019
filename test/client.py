import socket

# read test image to send over network
with open("test_image.png", "rb") as image:
    f = image.read()
    #b = bytearray(f)

HOST = "127.0.0.1"
PORT = 63222

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(f)  # sends a bytes object
    data = s.recv(600*530*3)

print(len(data))
print('Recieved', (data))

# import socket
# 
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect(("10.153.85.238", 1234))    # PC static IP
# #s.connect((socket.gethostname(), 1234))
# 
# msg = s.recv(1024)
# print(msg.decode("utf-8"))
 
