import cv2
import numpy as np
from matplotlib import pyplot as plt
 
img = cv2.imread('C:\Python27\Winter Project\Filters\sq.jpg',0)
cv2.imshow("original",img)
#h1=cv2.getGaussianKernel(5,5)
#rint h1
#10ingaussianFunction is deviation
blur = cv2.GaussianBlur(img,(7,7),10)
cv2.imshow("blurred",blur)
cv2.waitKey(0)
