import io
import socket
import struct
from PIL import Image

# Start a socket listening for connections on 0.0.0.0:8000 (0.0.0.0 means
# all interfaces)
server_socket = socket.socket()
#server_socket.bind((socket.gethostname(), 8000))
server_socket.bind(('0.0.0.0', 8000))
server_socket.listen(0)

# Accept a single connection and make a file-like object out of it
try:
    while True:
        c, a = server_socket.accept()
        connection = c.makefile('rb')
        # Read the length of the image as a 32-bit unsigned int. If the
        # length is zero, quit the loop
        image_len = struct.unpack('<L', connection.read(struct.calcsize('<L')))[0]
        if image_len:
            # Construct a stream to hold the image data and read the image
            # data from the connection
            image_stream = io.BytesIO()
            image_stream.write(connection.read(image_len))
            # Rewind the stream, open it as an image with PIL and do some
            # processing on it
            image_stream.seek(0)
            image = Image.open(image_stream)
            image.show()
            print('Image is %dx%d' % image.size)
            image.verify()
            print('Image is verified')
            c.send("Recieved Image!".encode('utf-8'))
        connection.close()
finally:
    server_socket.close()

