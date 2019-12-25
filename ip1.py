import cv2
import numpy as np
img = cv2.imread('TIMETABLE-page0001.jpg')
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,mask = cv2.threshold(img_gray, 220,255,cv2.THRESH_BINARY_INV)
mask_inv = cv2.bitwise_not(mask)
cv2.imshow('image',mask_inv)
