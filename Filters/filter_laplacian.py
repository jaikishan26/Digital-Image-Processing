import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('image.jpg',0)
cv2.imshow('input',img)
#blur = cv2.GaussianBlur(img,(5,5),10)
laplacian1 = cv2.Laplacian(img,cv2.CV_8U,ksize=5,scale=1,delta=1)
#laplacian2 = cv2.Laplacian(img,cv2.CV_64F,ksize=5,scale=1,delta=5)
plt.imshow(laplacian1,cmap = 'gray')
plt.show()
#plt.imshow(laplacian2,cmap = 'gray')
#plt.show()
#cv2.imshow('blurred',laplacian1)
#cv2.imshow('blurred1',laplacian2)
#cv2.waitKey(0)
