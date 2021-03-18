import cv2
import numpy as np
import matplotlib.pyplot as plt


def sharp(image, kernel):

    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    fig, ax = plt.subplots(1, figsize=(10,8))
    plt.imshow(image)
    img = cv2.filter2D(image, -1, kernel)
    fig, ax = plt.subplots(1, figsize=(10,8))
    plt.imshow(img)




if __name__ == '__main__':
    image = cv2.imread('imagen.jpg')
    cv2.imshow('image',image)
    kernel = np.array([[0, -1, 0],
                   [-1, 5, -1],
                   [0, -1, 0]])
    output = sharp(image, kernel)
    plt.show()
