import cv2
import numpy as np

# Harris Corner Detection
# Read the image and convert to greyscale
img = cv2.imread('img/corner0.png')
cv2.imshow('Ori', img)

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
 
# Find the corners using the Harris Corner Detector
dst = cv2.cornerHarris(gray,2,3,0.04)
 
#result is dilated for enhancing the corners, not important
dst = cv2.dilate(dst,None)
 
# Threshold for an optimal value, it may vary depending on the image.
thresh = 0.01*dst.max()
img[dst>thresh]=[0,255,0]
 
# Display the image
cv2.imshow('dst',img)
cv2.waitKey(0)
# ---------------------------------------------------------------------------
img = cv2.imread('img/corner0.png')
cv2.imshow('Ori', img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

corners = cv2.goodFeaturesToTrack(gray, 28, 0.01, 10)
corners = np.int0(corners)

for i in corners:
         x, y = i.ravel()
         cv2.circle(img, (x,y), 3, (0,0,255), -1)

cv2.imshow('Corners', img)

cv2.waitKey()
cv2.destroyAllWindows()
