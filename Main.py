import numpy as np
import cv2
import argparse
import matplotlib.pyplot as plt
from Sobel import sobel

def op1(image, kernel):
    sobel(image,kernel)


if __name__ == "__main__":
    image= cv2-imread("imagen.jpg")
    cv2.imshow("imagen",image)
    kernel = np.array ([[-1,-2,-1]
                        [0,0,0]
                        [1,2,1]])
    output= sobel(image,kernel)
    plt.show()
