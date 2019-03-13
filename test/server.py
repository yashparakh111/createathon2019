import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", 1234))
s.listen(1)

while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established!")
    clientsocket.send(bytes("Welcome to the server!", "utf-8"))

    clientsocket.close()

