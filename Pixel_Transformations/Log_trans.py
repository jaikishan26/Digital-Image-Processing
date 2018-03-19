import cv2
import numpy as np
from matplotlib import pyplot as plt

# Your code
img = cv2.imread('C:\Python27\Winter Project\Pixel_trans\ele.jpg')
cv2.imshow('input',img)
# New code
img2 = np.log10(1 + img.astype(np.float)).astype(np.uint8)
#calculating the pixel intensities which are there in this image2
b=np.unique(img2)
print b
#calculating the maximum of all the insentity values present in image2
c=np.amax(b)
print c
#scaling the image2 for better visuals
d=(255/c)
scale=d.astype(np.uint8)
print scale
# Back to your code
img2 = scale*img2 # Edit from before
cv2.imshow('LSP',img2)
cv2.waitKey(0)

