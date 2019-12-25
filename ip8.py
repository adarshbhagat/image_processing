import cv2
import numpy as np
img = cv2.imread('try.jpg')
img1 = cv2.imread('kiran.jpg')
width = int(1280)
height = int(720)
dim = (width,height)
img1 = cv2.resize(img1, dim, interpolation = cv2.INTER_NEAREST)
img2 = cv2.addWeighted(img,0.4,img1,0.6,0)
while 1:
    cv2.imshow('image',img2)
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.imwrite('beautiful.jpg',img2)
cv2.destroyAllWindows()
