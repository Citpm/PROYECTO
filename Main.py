import numpy as np
import cv2
import argparse
import matplotlib.pyplot as plt

import detectarbordes
import filtro_promedio
from filtro_sharpen import sharp


def a1(image, kernel):
    sharp(image,kernel)

def a2(image):
    detect_edge(image)



if __name__ == '__main__':


    x = '0'
    if x == '1':
        image = cv2.imread('imagen.jpg')
        kernel = np.array([[0, -1, 0],
                       [-1, 5, -1],
                       [0, -1, 0]])
        output = a1(image, kernel)
        plt.show()
    if x == '2':
        image = cv2.imread('imagen.jpg')
        output = a2(image)
