import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread('p2.jpg',0)
edges = cv.Canny(img,50,100)
plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Canny Image'), plt.xticks([]), plt.yticks([])
plt.show()
