import cv2
sift = cv2.xfeatures2d.SIFT_create()

"""
Aquí se crea un objeto sift utilizando el método cv2.xfeatures2d.SIFT_create()
"""

imagen = cv2.imread('imagen.jpg')
gray = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

sift = cv2.xfeatures2d.SIFT_create()
keypoints, descriptors = sift.detectAndCompute(gray, None)

print('Se encontraron', len(keypoints), 'puntos clave en la imagen.')

imagen_con_puntos_clave = cv2.drawKeypoints(gray, keypoints, None)
cv2.imshow('Imagen con puntos clave SIFT', imagen_con_puntos_clave)
cv2.waitKey()
cv2.destroyAllWindows()