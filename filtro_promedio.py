"""
By Unipython
code taken from https://unipython.com/suavizando-imagenes-con-opencv/

Modified by Citlali Pardo
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt
 
img = cv2.imread('imagen.jpg')
 
blur = cv2.blur(img,(3,3))
 
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Difuminada')
plt.xticks([]), plt.yticks([])
plt.show()