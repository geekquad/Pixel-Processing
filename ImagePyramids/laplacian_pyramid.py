
############Laplacian Pyramid############
import cv2
import numpy as np
image = cv2.imread("flower.jfif")
layers = image.copy()
gaussian_p = [layers]

for i in range(5):
    layers = cv2.pyrDown(layers) 
    gaussian_p.append(layers)
    #cv2.imshow(str(i), layers)

layers = gaussian_p[4]
cv2.imshow("this is upper level gaussian pyramid",layers)
lp = [layers]

for i in range(4, 0 ,-1):
    gaussian_extended = cv2.pyrUp(gaussian_p[i])
    laplacian = cv2.subtract(gaussian_p[i-1], gaussian_extended)
    cv2.imshow(str(i), laplacian)

cv2.imshow("original image", image)
cv2.waitkey(0)
cv2.destroyAllWindows()
