"Modified by Melissa Robles García A01637961"
import cv2
import numpy as np
import matplotlib.pyplot as plt


def sobel(image, kernel):
    
    image =cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    fig, ax =plt.subplots(1, figsize=(10,8))
    plt.imshow(image)
    img = cv2.filter2D(image, -1, kernel)
    fig, ax = plt.subplots(1, figsize=(10,8))
    plt.imshow(img)

    
    
    
if __name__ == "__main__":
    image = cv2.imread("imagen.jpg")
    cv2.imshow("image",image)
    kernel = np.array ([[-1,-2,-1]
                        [0,0,0]
                        [1,2,1]])
    output = sobel(image, kernel)
    plt.show()
