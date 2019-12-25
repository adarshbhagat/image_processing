import cv2
import numpy as np
img=cv2.imread("TIMETABLE.jpg")
img=cv2.bitwise_not(img)

cv2.imwrite('try_modidy.jpg',img)
