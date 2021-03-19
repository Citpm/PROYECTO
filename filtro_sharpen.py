"Modified by Ernesto Del Toro Sánchez A01638191"
import cv2 #Utilizamos esta librería para todo el análisis y muestreo de imáenes
import numpy as np
import matplotlib.pyplot as plt #Matplotlib es usada para la visualización de graficas, la usamos para acomodar las do fotos juntas


def sharp(image, kernel): #Definimos una función que tome la imagen seleccionada y el Kernel para el efecto deseado

    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    plt.imshow(image)
    img = cv2.filter2D(image, -1, kernel) #La función de filter2D es hacer una convolución entre la imagen y el Kernel
    plt.subplot(121),plt.imshow(image),plt.title('Original') #Gracias a matplotlib podemos acomodar las fotos iniciales y resultantes con sus respectivos t{itulos}
    plt.subplot(122),plt.imshow(img),plt.title('Sharp')





image = cv2.imread('imagen.jpg') #Leemos la imagen a la cual le aplicaremos los filtros

kernel = np.array([[0, -1, 0],   #Configuramos el kernel para el filtro deseado 
                   [-1, 5, -1],
                   [0, -1, 0]])
output = sharp(image, kernel)
plt.show()
