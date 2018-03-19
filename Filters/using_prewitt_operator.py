import cv2
import numpy as np
import math
from matplotlib import pyplot as plt

img = cv2.imread('C:\Python27\Winter Project\Filters\sdf.jpg',0)
cv2.imshow("original",img) 
 

kernelx = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
kernely = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
img_prewittx = cv2.filter2D(img, -1, kernelx)
img_prewitty = cv2.filter2D(img, -1, kernely)
#ddepth=-1 means that the output image has same depth as input image
cv2.imshow('prewitt_x',img_prewittx)
cv2.imshow('prewitt_y',img_prewitty)
cv2.waitKey(0)
cv2.destroyAllWindows()
