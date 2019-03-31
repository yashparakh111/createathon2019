import picamera
import io
import time
import cv2
import numpy as np

from skimage.measure import compare_ssim as ssim
from skimage.measure import compare_mse as mse
from skimage.measure import compare_nrmse as nrmse

from Image_Classification import *

# initialize camera object
camera = picamera.PiCamera()
camera.resolution(640, 480) 

def capture_image():
    # Create in-memory stream and capture image to it
    stream = io.BytesIO()
    with picamera.PiCamera() as camera:
        time.sleep(2)       # allow camera to warm up
        camera.resolution(640, 480)
        camera.capture(stream, format='jpeg')

    # Construct a numpy array from the stream
    trash_object_data = np.fromstring(stream.getvalue(), dtype=np.uint8)

    # Read image to array with openCV
    trash_object_image = cv2.imread(trash_object_data, 1)
    #trash_object_image = trash_object_image[:, :, ::-1]     # convert from BGR to RGB

    return trash_object_image, stream

# initialize image differencing thresholds
mse_threshold = 1000
ssim_threshold = 1000
nrmse_threshold = 1000

def confirmObjectPresence():
    # capture trash object image
    trash_object_image, stream = capture_image()

    # read empty receptacle image
    empty_receptacle_image = cv2.imread("empty_receptacle.jpg")

    # convert image to grayscale
    empty_receptacle_image = cv2.cvtColor(empty_receptacle_image, cv2.COLOR_BRG2GRAY)
    trash_object_image = cv2.cvtColor(trash_object_image, cv2.COLOR_BRG2GRAY)

    # Compute mean squared error and structural similarity
    m = mse(empty_receptacle_image, trash_object_image)
    s = ssim(empty_receptacle_image, trash_object_image)
    n = nrmse(empty_receptacle_image, trash_object_image)

    if(m > mse_threshold):
        return classifyImage(stream)
