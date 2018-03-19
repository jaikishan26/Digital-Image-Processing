import cv2
import numpy as np
from matplotlib import pyplot as plt
 
img = cv2.imread('C:\Python27\Winter Project\Filters\sq.jpg')
cv2.imshow("original",img) 
 
kernel = np.ones((5,5),np.float32)
kernel[2,2]=5
kernel = kernel/29
print kernel
dst = cv2.filter2D(img,-1,kernel)
cv2.imshow("blurred",dst)
cv2.waitKey(0)
