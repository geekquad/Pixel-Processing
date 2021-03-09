import cv2
import numpy as np

count=0
img_hough = cv2.imread('resource/soduky_img.jpg')
img_circles=cv2.imread('resource/ball_ref_img.jpg')
gray_circle=cv2.cvtColor(img_circles,cv2.COLOR_BGR2GRAY)
img_hough_PL=img_hough.copy()
gray_img = cv2.cvtColor(img_hough,cv2.COLOR_BGR2GRAY)
canny_img = cv2.Canny(gray_img,50,150,apertureSize = 3)
minLineLength=80
maxLineGap=15
Hough_lines = cv2.HoughLines(canny_img,1,np.pi/180,150,None,0,0)
Houghlines_PL = cv2.HoughLinesP(canny_img,1,np.pi/180,100,minLineLength,maxLineGap)


for rho,theta in Hough_lines[0]:
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(a))

    cv2.line(img_hough,(x1,y1),(x2,y2),(0,0,255),2)
for x1,y1,x2,y2 in Houghlines_PL[0]:
    cv2.line(img_hough_PL,(x1,y1),(x2,y2),(0,255,0),2)

circles = cv2.HoughCircles(gray_circle, cv2.HOUGH_GRADIENT, 1, 40, param1=40, param2=40, minRadius=10, maxRadius=60)
if circles is not None:
    # convert the (x, y) coordinates and radius of the circles to integers
    circle1 = np.round(circles[0, :]).astype("int")
    # loop over the (x, y) coordinates and radius of the circles
    for (x, y, r) in circle1:
        cv2.circle(img_circles, (x, y), r, (0, 255, 0), 3)
cv2.imshow('Houghlines',img_hough)
cv2.imshow('Probablisitic Hough Lines',img_hough_PL)
cv2.imshow('HoughCircles',img_circles)

cv2.waitKey(0)