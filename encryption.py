import cv2
import numpy as np
img=cv2.imread("try.jpg")
img=cv2.resize(img, (300,300))
height, width, channels = img.shape
j=int(0)
count = int(0)
for q in range(2):
    for i in range(300):
        j=int(0)
        while(74+j<=149 and 74-j>=0):
            #swap(74+j,299-2j+1)
            temp0=img[i][74+j][0]
            temp1=img[i][74+j][1]
            temp2=img[i][74+j][2]
            img[i][74+j]=img[i][299-((2*j)+1)]
            img[i][299-((2*j)+1)][0]=temp0
            img[i][299-((2*j)+1)][1]=temp1
            img[i][299-((2*j)+1)][2]=temp2
            #swap(74-j,299-2j)
            temp0=img[i][74-j][0]
            temp1=img[i][74-j][1]
            temp2=img[i][74-j][2]
            img[i][74-j]=img[i][299-(2*j)]
            img[i][299-(2*j)][0]=temp0
            img[i][299-(2*j)][1]=temp1
            img[i][299-(2*j)][2]=temp2
            j+=1
    for i in range(300):
        j=int(0)
        while(74+j<=149 and 74-j>=0):
            #swap(74-j,299-2j)
            temp0=img[74-j][i][0]
            temp1=img[74-j][i][1]
            temp2=img[74-j][i][2]
            img[74-j][i]=img[299-(2*j)][i]
            img[299-(2*j)][i][0]=temp0
            img[299-(2*j)][i][1]=temp1
            img[299-(2*j)][i][2]=temp2
            #swap(74+j,299-2j+1)
            temp0=img[74+j][i][0]
            temp1=img[74+j][i][1]
            temp2=img[74+j][i][2]
            img[74+j][i]=img[299-((2*j)+1)][i]
            img[299-((2*j)+1)][i][0]=temp0
            img[299-((2*j)+1)][i][1]=temp1
            img[299-((2*j)+1)][i][2]=temp2
            j+=1
cv2.imwrite('try_modidy.jpg',img)
