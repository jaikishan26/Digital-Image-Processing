import cv2
import numpy as np
import math
from matplotlib import pyplot as plt
img=cv2.imread('C:\Python27\Winter Project\histogram\image1.jpg',0)
cv2.imshow('input',img)
plt.hist(img.ravel(),256,[0,256]);
plt.show()
height = img.shape[0]
width = img.shape[1]
for i in np.arange(height):
    for j in np.arange(width):
        a= img.item(i,j)
        if a > max:
            max=a
        if a <min:
            min=a
max1= np.max(img)
min1=np.min(img)
for i in np.arange(height):
    for j in np.arange(width):
        a= img.item(i,j)
        b=(float(a-min1)/(max1-min1))*255
        img.itemset((i,j),b)
cv2.imwrite('C:\Python27\Winter Project\histogram\cars.jpg',img)
cv2.imshow('car4',img)
plt.hist(img.ravel(),256,[0,256]);
plt.show()

Smin=40
Smax=90
Rmin=2
Rmax=30
s1 =(Smin/Rmin)
s2=(float(Smax-Smin)/Rmax-Rmin)
s3=(float(255-Smax)/(255-Rmax))

for i in np.arange(height):
    for j in np.arange(width):
        a = img.item(i,j)
        if 0< a <Rmin:
            b = s1*a
        elif Rmin< a <Rmax:
            b = (s2*a + Smin)
        else:
            b = (s3*a + Smax)
        img.itemset((i,j),b)
cv2.imwrite('C:\Python27\Winter Project\histogram\cars1.jpg',img)
#plt.hist(img.ravel(),256,[0,256plt.show()

#cv2.imshow('car5',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
