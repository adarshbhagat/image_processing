import cv2
import numpy as np
video=cv2.VideoCapture(0)
lower_red=np.array([229,102,102])
upper_red=np.array([255,0,0])
while True:
    _,frame=video.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv,lower_red,upper_red)
    res = cv2.bitwise_and(frame,frame,mask = mask)
    cv2.rectangle(frame,(125,50),(50,125),(255,255,255),5)
    cv2.imshow('only hsv',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()
