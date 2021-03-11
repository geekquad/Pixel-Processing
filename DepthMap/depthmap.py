import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

# reading the image of a very slight left angle
imgL = cv.imread('assets\left.jpg',0)
# reading the image of a very slight right angle
imgR = cv.imread('assets\right.jpg',0)

# Stereo BM stands for block matching algorithm
stereo = cv.StereoBM_create(numDisparities=16, blockSize=15)
disparity = stereo.compute(imgL,imgR)
plt.imshow(disparity,'gray')
plt.show()

''''
Here are a few parameters, tuning of which will yield in better results.

minDisparity - Minimum possible disparity value.
numDisparities - Maximum disparity minus minimum disparity. This parameter must be divisible by 16.
SADWindowSize - Matched block size. It must be an odd number >=1 .
disp12MaxDiff - Maximum allowed difference (in integer pixel units) in the left-right disparity check.
preFilterCap - Truncation value for the prefiltered image pixels.
uniquenessRatio - Margin in percentage by which the best (minimum) computed cost function value should "win" the second best value to consider the found match correct. Normally, a value within the 5-15 range is good enough.
speckleWindowSize - Maximum size of smooth disparity regions to consider their noise speckles and invalidate.
speckleRange - Maximum disparity variation within each connected component.

'''''