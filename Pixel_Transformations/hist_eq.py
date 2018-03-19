import cv2
import numpy as np
import math
from matplotlib import pyplot as plt
img = cv2.imread('C:\Python27\Winter Project\histogram\car.jpg',0)
cv2.imshow('Car2',img)
def histogram(img):
    height = img.shape[0]
    width=img.shape[1]

    hist=np.zeros((256))

    for i in np.arange(height):
        for j in np.arange(width):
            a = img.item(i,j)
            hist[a] += 1

    return hist

def cumulative_histogram(hist):
    cum_hist=hist.copy()

    for i in np.arange(1,256):
        cum_hist[i]=cum_hist[i-1]+cum_hist[i]

    return cum_hist



height = img.shape[0]
width = img.shape[1]
pixels = width*height
hist = histogram(img)
cum_hist = cumulative_histogram(hist)
plt.hist(img.ravel(),256,[0,256]);
plt.show()

for i in np.arange(height):
    for j in np.arange(width):
        a=img.item(i,j)
        b=math.floor(cum_hist[a]*255.0/pixels)
        img.itemset((i,j),b)

img1=cv2.imwrite('C:\Python27\car1.jpg',img)

cv2.imshow("care",img)
plt.hist(img.ravel(),256,[0,256]);
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
