#By DEV
#Code taken from: https://dev.to/kalebu/how-to-detect-edges-in-an-image-using-opencv-in-python-12cm

#Modified by Diego Rosas

import cv2
import matplotlib.pyplot as plt 

def detect_edge(image):
    ''' Funcion para detectar bordes '''

    image_with_edges = cv2.Canny(image , 100, 200)

    images = [image , image_with_edges]

    location = [121, 122]

    for loc, img in zip(location, images):
        plt.subplot(loc)
        plt.imshow(img, cmap='gray')

    plt.savefig('borde.png')
    plt.show()

image = cv2.imread('imagen.jpg', 0)
detect_edge(image)