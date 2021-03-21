import cv2
import numpy as np

img_hough = cv2.imread("resource/soduky_img.jpg") #Reading the image
img_circles=cv2.imread("resource/ball_ref_img.jpg")
gray_circle=cv2.cvtColor(img_circles,cv2.COLOR_BGR2GRAY) #Applying gray filter
gray_img = cv2.cvtColor(img_hough,cv2.COLOR_BGR2GRAY)
canny_img = cv2.Canny(gray_img,50,150,apertureSize = 3) #Applying cannny edge detection
minimum_line_length=80
maximum_line_gap=15
Houghlines_PL = cv2.HoughLinesP(canny_img,1,np.pi/180,80,minimum_line_length,maximum_line_gap) #Applying probablistic Hough lines

for x1,y1,x2,y2 in Houghlines_PL[0]:
    cv2.line(img_hough,(x1,y1),(x2,y2),(0,255,0),2) #Drawing the detected lines

circles = cv2.HoughCircles(gray_circle, cv2.HOUGH_GRADIENT, 1, 40, param1=40, param2=40, minRadius=10, maxRadius=60) # Applying Hough Circles

if circles is not None:
    circle1 = np.round(circles[0, :]).astype("int")
    for (x, y, r) in circle1:
        cv2.circle(img_circles, (x, y), r, (0, 255, 0), 3) #Drawing the detected circles

cv2.imshow("Probablisitic Hough Lines",img_hough) #Displaying the result after applying Probablisitic Hough Lines.
cv2.imshow("Hough Circles",img_circles) # Displaying the result after applying Hough Circles
cv2.waitKey(0)