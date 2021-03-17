import cv2

img = cv2.imread('resources/ref_img.jpg')
gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
sobel_imgx=cv2.Sobel(gray_img,cv2.CV_64F,1,0,ksize=-1)
sobel_imgy=cv2.Sobel(gray_img,cv2.CV_64F,0,1,ksize=-1)
canny_img = cv2.Canny(gray_img,100,100)
cv2.imshow("Actual image",img)
cv2.imshow("Canny Image",canny_img)
cv2.imshow("Sobel Image in x-direction", sobel_imgx)
cv2.imshow("Sobel Image in y-direction", sobel_imgy)
cv2.waitKey(0)






