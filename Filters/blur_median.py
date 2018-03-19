import cv2
import numpy as np
from matplotlib import pyplot as plt
 
img = cv2.imread('C:\Python27\Winter Project\Filters\img.jpg')
cv2.imshow("original",img)

blur= cv2.medianBlur(img,5)
cv2.imshow("blurred",blur)
cv2.waitKey(0)
