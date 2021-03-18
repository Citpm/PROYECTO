"Modified by Ernesto Del Toro Sánchez A01638191"
import cv2
import numpy as np
import matplotlib.pyplot as plt


def sharp(image, kernel):

    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    plt.imshow(image)
    img = cv2.filter2D(image, -1, kernel)
    plt.subplot(121),plt.imshow(image),plt.title('Original')
    plt.subplot(122),plt.imshow(img),plt.title('Sharp')





image = cv2.imread('imagen.jpg')

kernel = np.array([[0, -1, 0],
                   [-1, 5, -1],
                   [0, -1, 0]])
output = sharp(image, kernel)
plt.show()
