import cv2
import numpy as np
import math
from matplotlib import pyplot as plt


def cumulative_histogram(hist):
    cum_hist=hist.copy()

    for i in np.arange(1,256):
        cum_hist[i]=cum_hist[i-1]+cum_hist[i]

    return cum_hist

def histogram(img):
    height = img.shape[0]
    width=img.shape[1]

    hist=np.zeros((256))

    for i in np.arange(height):
        for j in np.arange(width):
            a = img.item(i,j)
            hist[a] += 1

    return hist


def hist_match(img,img_ref):
 

    height = img.shape[0]
    width = img.shape[1]
    pixels = width*height
    hist = histogram(img)
    hist_ref = histogram(img_ref)
                      
    cum_hist = cumulative_histogram(hist)
    cum_hist_ref= cumulative_histogram(hist_ref)
                      
    #plt.hist(img.ravel(),256,[0,256]);
    #plt.show()
    #plt.hist(img_ref.ravel(),256,[0,256]);
    #plt.show()

    height_ref = img_ref.shape[0]
    width_ref = img_ref.shape[1]
    pixels_ref = width_ref*height_ref

    prob_cum_hist = cum_hist/pixels
    prob_cum_hist_ref= cum_hist_ref/pixels_ref


    K=256
    new_values = np.zeros((K))

    for a in np.arange(K):
        j=K-1
        while True:
            new_values[a] = j
            j=j-1
            if j<0 or prob_cum_hist[a] > prob_cum_hist_ref[j]:
                break

    for i in np.arange(height):
        for j in np.arange(width):
            a=img.item(i,j)
            b=math.floor(cum_hist[a]*255.0/pixels)
            img.itemset((i,j),b)

    return img
