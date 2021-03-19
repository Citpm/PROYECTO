import numpy as np
import cv2
import argparse
import matplotlib.pyplot as plt

import detectarbordes
import filtro_promedio
from filtro_sharpen import sharp
from Sobel import sobel


def a1(image, kernel):
    sharp(image,kernel)

def a2(image):
    detect_edge(image)



if __name__ == '__main__':


    x = '0'
