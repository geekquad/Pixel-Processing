#importing libraries
import numpy as np
import cv2
from matplotlib import pyplot as plt

#load left and right image and convert it into grayscale
left = cv2.imread('Left.jpg',0)

right = cv2.imread('right.jpg',0)

#applying disparity
stereo = cv2.StereoBM_create(numDisparities=96, blockSize=15)

depth = stereo.compute(left,right)

plt.figure(figsize = (18,8))

plt.imshow(depth,'disparity')

plt.xticks([])

plt.yticks([])

