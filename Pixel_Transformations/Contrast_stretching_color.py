import cv2
import numpy as np
import math
from matplotlib import pyplot as plt
import stretch
img = cv2.imread('C:\Python27\Winter Project\histogram\image1.jpg')
cv2.imshow('input',img)
b,g,r = cv2.split(img)
blue = stretch.con_stretch(b)
green = stretch.con_stretch(g)
red = stretch.con_stretch(r)
x=cv2.merge((blue,green,red))
cv2.imshow("eeee" ,x)
cv2.waitKey(0)
