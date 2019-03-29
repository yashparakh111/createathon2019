import numpy as np
import cv2
import sys

backgroundSubtractor = cv2.createBackgroundSubtractorMOG2()

# apply the algorithm for background images using learning rate > 0

bg = cv2.cvtColor(cv2.imread('background.jpg'), cv2.COLOR_BGR2GRAY)
backgroundSubtractor.apply(bg, learningRate = 0.9)

stillFrame = cv2.cvtColor(cv2.imread('object.jpg'), cv2.COLOR_BGR2GRAY)
fgmask = backgroundSubtractor.apply(stillFrame, learningRate = 0)

#show both images
im_shape = (bg.shape[0]/8, bg.shape[1]/2)
cv2.imshow('background', cv2.resize(bg, im_shape))
cv2.imshow('object', cv2.resize(stillFrame, im_shape))
cv2.imshow('changed', cv2.resize(fgmask, im_shape))
cv2.waitKey()
cv2.destroyAllWindows()

