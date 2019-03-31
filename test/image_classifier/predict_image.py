import numpy as np
from keras import backend as K
from keras.applications.resnet50 import ResNet50
from keras.models import load_model
from keras.preprocessing.image import ImageDataGenerator, load_img
from sklearn.metrics import classification_report, confusion_matrix
from PIL import Image
import os

TRAIN_BATCH_SIZE = 8
TEST_BATCH_SIZE = 8
MAX_TRAIN_IMAGE_COUNT = 1000
MAX_TEST_IMAGE_COUNT = 32
EPOCHS = 50
IMG_HEIGHT = 576
IMG_WIDTH = 432
categories = ["Compost", "Landfill", "Recycle"]

model = load_model('best_model_84.h5')
test_path = 'test_images'
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

