import cv2
path=input("Enter the path : ") 
#Read the image
image = cv2.imread(path)
#Convert the color image to HSV image
hsv= cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
#Displaying of HSV iamge
cv2.imshow('HSV image', hsv)
#Saving of image
cv2.imwrite("hsv_image.png",hsv)
cv2.waitKey(0)#wait for the key event
cv2.destroyAllWindows()
