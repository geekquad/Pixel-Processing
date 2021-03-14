"""
Robert Edge Detection
"""

import cv2 as cv
import numpy as np
import math

# function to compute convolution between kernel and original image
def compute_convolution(input_image, kernel):
    width = input_image.shape[0]
    height = input_image.shape[1]
        
    # Middle of the kernel
    offset = len(kernel) // 2

    # Create empty output array
    output_image = np.empty((width,height))
    output_image.fill(0)

    # Compute convolution between value and Robert kernels
    for x in range(offset, width - offset):
        for y in range(offset, height - offset):
            for a in range(len(kernel)):
                for b in range(len(Rx)):
                    xn = x + a - offset
                    yn = y + b - offset
                    value = input_image[xn][yn]
                    output_image[x][y] += value * kernel[a][b]
                output_image[x][y] = math.sqrt(output_image[x][y]**2)
    return output_image



#-----------------------Main Function----------------------#

# reading an image in grayscale
img_gray = cv.imread('Robert_EdgeDetection_img.jpg', 0)

# Robert Mask Operator
Rx = [[ 1,  0], 
      [ 0, -1,]]

Ry = [[ 0,  1], 
      [-1,  0]]

# computing image formed by convolution with kernel Rx
robert_x = compute_convolution(img_gray, Rx)
# computing image formed by convolution with kernel Ry
robert_y = compute_convolution(img_gray, Ry)

# getting the final edge detected image by combining the two convolutions using gradient formula
output_img = np.empty((robert_x.shape[0], robert_x.shape[1]))
for i in range(robert_x.shape[0]):
    for j in range(robert_x.shape[1]):
        output_img[i][j] = math.sqrt(robert_x[i][j]**2 + robert_y[i][j]**2)

#saving edge detected image
cv.imwrite("Robert_EdgeDetection_output.jpg", output_img)
