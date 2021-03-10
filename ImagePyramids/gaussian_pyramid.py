''' image pyramids are of two type that are:
1.Gaussian pyramid
2.Laplacian pyramid
below is the implemntation of gaussian pyramid using pyrDown()
fuction upto 5 levels'''

##########Gaussian Image Pyramid###############3
import cv2
import numpy as np
image = cv2.imread("flower.jfif")
layers = image.copy()
gaussian_p = [layers]

for i in range(5):
    layers = cv2.pyrDown(layers) 
    gaussian_p.append(layers)
    cv2.imshow(str(i), layers)

cv2.imshow("original image", image)
cv2.waitkey(0)
cv2.destroyAllWindows()
