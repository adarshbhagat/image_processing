import cv2
import numpy as np
img = cv2.imread('try.jpg')
img[500,420]=[255,0,0]
cv2.imshow('image',img)
