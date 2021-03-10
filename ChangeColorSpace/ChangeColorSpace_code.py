import cv2
import numpy as np
img=cv2.imread("resource/ball_ref_img.jpg")
gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
hsv_img=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cv2.imshow("Gray Scale Image",gray_img)
cv2.imshow("HSV scale Image",hsv_img)
cv2.waitKey(0)
