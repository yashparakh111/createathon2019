import socket

HOST = "127.0.0.1"
PORT = 63222

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True: # keep listening for client
            data = conn.recv(600*530*3)  # listens for a bytes object
            if not data:
                break
            conn.sendall(data)

# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.bind(("127.0.0.1", 1234))
# s.listen(1)
# 
# while True:
#     clientsocket, address = s.accept()
#     print(f"Connection from {address} has been established!")
#     clientsocket.send(bytes("Welcome to the server!", "utf-8"))
# 
#     clientsocket.close()

