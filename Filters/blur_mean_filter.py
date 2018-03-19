import cv2
import numpy as np
from matplotlib import pyplot as plt
 
img = cv2.imread('C:\Python27\Winter Project\Filters\sq.jpg',0)
cv2.imshow("original",img) 
 
kernel = np.ones((5,5),np.float32)/25
dst = cv2.filter2D(img,-1,kernel)
cv2.imshow("blurred",dst)
cv2.waitKey(0)
#plt.subplot(121)
#plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
#plt.show()
#plt.title('Original')
#plt.xticks([])
#plt.subplot(122)
#plt.imshow(cv2.cvtColor(dst,cv2.COLOR_BGR2RGB))
#plt.show()
#plt.title('Averaging')
#plt.xticks([])
#plt.yticks([])
#plt.show()
