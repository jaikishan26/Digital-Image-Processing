import cv2
import numpy as np
import math
from matplotlib import pyplot as plt
def con_stretch(img):
    
    height = img.shape[0]
    width = img.shape[1]
    max1= np.max(img)
    min1=np.min(img)
    for i in np.arange(height):
        for j in np.arange(width):
            a= img.item(i,j)
            b=(float(a-min1)/(max1-min1))*255
            img.itemset((i,j),b)
    #cv2.imwrite('C:\Python27\Winter Project\histogram\cars.jpg',img)
    #cv2.imshow('car4',img)

    Smin=15
    Smax=180
    Rmin=5
    Rmax=60
    slope=(float(Smax-Smin)/Rmax-Rmin)
    for i in np.arange(height):
        for j in np.arange(width):
            a = img.item(i,j)
            if 5< a <80:
                b = (slope*(a-5) + Smin)
            else:
                b = a
            img.itemset((i,j),b)
#cv2.imwrite('C:\Python27\Winter Project\histogram\cars1.jpg',img)

#cv2.waitKey(0)
#cv2.destroyAllWindows()
    return img
