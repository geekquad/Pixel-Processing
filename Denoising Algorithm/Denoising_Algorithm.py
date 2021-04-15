'''
  For using this Script you need to install OpenCV in your machine
'''
#Importing openCV library
import cv2 as cv

#Taking path of input from the user
path=input("Enter the path of uploaded image: ")
img=cv.imread(path)
img=cv.resize(img,(640,640))  #resizing the image

#Display the input image
cv.imshow('Input_Image',img)

#Excueting the Denoising Algorithm
dst = cv.fastNlMeansDenoisingColored(img,None,10,10,7,21)
cv.imshow('Output_image',dst)

cv.waitKey(0)
cv.destroyAllWindows()
