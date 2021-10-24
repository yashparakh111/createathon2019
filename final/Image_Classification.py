import io
import socket
import struct
import time

client_socket = socket.socket()
client_socket.connect(('10.145.73.172', 8000))
connection = client_socket.makefile('wb')
print("Making Connection to Image Classification Server:", str(connection))

def classifyImage(stream):
    try:
        # Write the length of capture and make sure everything is sent
        connection.write(struct.pack('<L', stream.tell()))
        connection.flush()

        # Rewind the stream and send the image data over the wire
        stream.seek(0)
        connection.write(stream.read())

        #connection.write(struct.pack('<L', 0))
        classification = client_socket.recv(1000)
        print("Here!")
    finally:
        print("Should close connection here")
        # client_socket.close()
        # connection.close()

    return classification
