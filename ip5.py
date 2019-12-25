import cv2
import numpy as np
img = cv2.imread('try.jpg')
img = cv2.circle(img,(447,63), 63, (0,0,255),10)
#img = cv2.flip(img,1)
cv2.imshow('image',img)
