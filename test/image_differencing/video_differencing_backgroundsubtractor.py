import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)
fgbg = cv.createBackgroundSubtractorKNN()

while(1):
    ret, frame = cap.read()
    fgmask = fgbg.apply(frame)
    cv.imshow('frame',fgmask)
    k = cv.waitKey(30) & 0xff
    if k == 27:
        break
cap.release()
cv.destroyAllWindows()
