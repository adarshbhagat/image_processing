import cv2
import numpy as np
cap = cv2.VideoCapture(0)
while 1:
    _,frame = cap.read()
    
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_red = np.array([100,136,24])
    upper_red = np.array([179,255,255])
    red_mask = cv2.inRange(hsv_frame, lower_red, upper_red)
    red = cv2.bitwise_and(frame, frame,mask=red_mask)
    cv2.imshow('frame', frame)
    cv2.imshow('red', red)
    cv2.imshow('red_mask', red_mask)
    if cv2.waitKey(5)==27:
        break
cv2.destroyAllWindows()
