import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import glob
import os

# Obtener la ruta de la carpeta con las imágenes
ruta_carpeta = "MANGO/"

# Obtener la lista de archivos de imagen en la carpeta
lista_imagenes = glob.glob(ruta_carpeta + "*.jpg")

# Ruta de salida para las imágenes procesadas
ruta_salida = "RESIZE_IMAGENES_SALIDA/GAUSSIANO/MANGO/"

# Crea el kernel 
kernel = np.ones((3,3),np.float32)/9 
kernel1 = np.ones((5,5),np.float32)/25
kernel2 = np.ones((7,7),np.float32)/49

# Crea la carpeta si no existe
os.makedirs(ruta_salida, exist_ok=True)

# Procesa cada imagen
for imagen in lista_imagenes:
    img = cv.imread(imagen)
    
    # Filtra la imagen utilizando el kernel anterior 
  #  dst = cv.GaussianBlur(img,(5,5),0) 
    dst2 = cv.GaussianBlur(img, (3,3),0)
    #dst2 = cv.GaussianBlur(img, (7,7),0)
    plt.figure(figsize=(15,8))

    plt.subplot(141),plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB)),plt.title('Original') 
 
    plt.xticks([]), plt.yticks([]) 
    plt.subplot(142),plt.imshow(dst2),plt.title('Gausiano 3*3') 
    plt.xticks([]), plt.yticks([]) 
   # plt.subplot(143),plt.imshow(dst),plt.title('Gausiano 5*5') 
   # plt.xticks([]), plt.yticks([]) 
   # plt.subplot(144),plt.imshow(dst2),plt.title('Gausiano 7*7') 
  #  plt.xticks([]), plt.yticks([]) 
    
    # Guarda la imagen en la ruta de salida especificada
    nombre_archivo = os.path.basename(imagen)
    plt.savefig(os.path.join(ruta_salida, nombre_archivo))
    
    plt.show()
