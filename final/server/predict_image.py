import numpy as np
from keras import backend as K
from keras.applications.resnet50 import ResNet50
from keras.models import load_model
from keras.preprocessing.image import ImageDataGenerator, load_img
from sklearn.metrics import classification_report, confusion_matrix
from PIL import Image
import os

import io
import socket
import struct
from PIL import Image

# ------------------SETUP ML CODE----------------------
TRAIN_BATCH_SIZE = 8
TEST_BATCH_SIZE = 8
MAX_TRAIN_IMAGE_COUNT = 1000
MAX_TEST_IMAGE_COUNT = 32
EPOCHS = 50
IMG_HEIGHT = 576
IMG_WIDTH = 432
categories = ["Compost", "Landfill", "Recycle"]
'''
test_path = 'test_images/Landfill'

print("Model Successfully loaded!")
test_datagen = ImageDataGenerator()
test_generator = test_datagen.flow_from_directory(test_path, target_size = (IMG_HEIGHT, IMG_WIDTH),
                                                               batch_size = 1, class_mode = 'categorical', shuffle = True)

test_path = "test_images/Landfill"
# Load and resize the image
img = load_img(os.path.join(test_path, os.listdir(test_path)[0]), target_size = (IMG_HEIGHT, IMG_WIDTH))
img = np.expand_dims(img, axis = 0)

#Confusion Matrix and Classification Report
test_generator.reset()
y = model.evaluate_generator(test_generator, steps = 3, verbose = 1)
print(y)

res = model.predict(img, verbose = 1)
print("Predicted image: ")
print(res.argmax(axis = -1))

test_generator.reset()
Y_pred = model.predict_generator(test_generator, steps = 3, verbose = 1)
print(Y_pred)
y_pred = np.argmax(Y_pred, axis=1) 
print('Confusion Matrix')
print(confusion_matrix(test_generator.classes, y_pred))
print('Classification Report')
print(classification_report(test_generator.classes, y_pred, target_names=categories))
'''

model = load_model('best_model_84.h5')
print('Model Successfully loaded!')

#img = load_img(os.path.join(test_path, os.listdir(test_path)[0]), target_size = (IMG_HEIGHT, IMG_WIDTH))
#img = np.expand_dims(img, axis = 0)

# ------------------SETUP SERVER CODE---------------------- 
# Start a socket listening for connections on 0.0.0.0:8000 (0.0.0.0 means
# all interfaces)
server_socket = socket.socket()
#server_socket.bind((socket.gethostname(), 8000))
server_socket.bind(('0.0.0.0', 8000))
server_socket.listen(0)

# Accept a single connection and make a file-like object out of it
try:
    c, a = server_socket.accept()
    while True:
        connection = c.makefile('rb')

        # Read the length of the image as a 32-bit unsigned int. If the
        # length is zero, quit the loop
        image_len = struct.unpack('<L', connection.read(struct.calcsize('<L')))[0]
        print("Image Len:", image_len)

        if image_len:
            # Construct a stream to hold the image data and read the image
            # data from the connection
            image_stream = io.BytesIO()
            image_stream.write(connection.read(image_len))

            # Rewind the stream, open it as an image with PIL and do some
            # processing on it
            image_stream.seek(0)
            image = Image.open(image_stream)

            # predict image model
            image_ml = np.array(image)
            image_ml = np.expand_dims(image, axis = 0)
            result = model.predict(image_ml, verbose = 1)

            # print results
            predicted_category = result.argmax(axis = -1)
            print("Predicted Image:", predicted_category[0])        # Send back predicted_category[0]

            image.show()
            print('Image is %dx%d' % image.size)
            image.verify()
            print('Image is verified')

            # send back classification
            c.send(str(predicted_category[0]).encode('utf-8'))
        connection.close()
finally:
    server_socket.close()
