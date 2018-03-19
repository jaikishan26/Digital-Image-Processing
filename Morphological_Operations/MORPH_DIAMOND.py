# Python program to demonstrate erosion and 
# dilation of images.
import cv2
import numpy as np
 
# Reading the input image
img = cv2.imread('color.JPG', 1)

#using DIAMOND element
# Taking a matrix of size 5*5 as the kernel#
M = np.zeros((5, 5), dtype=np.uint8)
M[2,2]=1
k1 = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
kernel = cv2.dilate(M, k1, iterations=2)



 
# The first parameter is the original image,
# kernel is the matrix with which image is 
# convolved and third parameter is the number 
# of iterations, which will determine how much 
# you want to erode/dilate a given image. 
img_erosion = cv2.erode(img, kernel, iterations=1)
img_dilation = cv2.dilate(img, kernel, iterations=1)
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel,iterations=4)
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel,iterations=2)
Morphologicalgradient=cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)

 
cv2.imshow('Input', img)
cv2.imshow('Erosion', img_erosion)
cv2.imshow('Dilation', img_dilation)
cv2.imshow('opening',opening)
cv2.imshow('closing',closing)
cv2.imshow('Gradient',Morphologicalgradient)
cv2.imshow('TOPHAT',tophat)
cv2.imshow('Blackhat',blackhat)
cv2.waitKey(0)
