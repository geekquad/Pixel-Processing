import cv2
path=input("Enter the path : ") 
#Read the image
image = cv2.imread(path)
#Convert the color image to Gray Scale image
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#Displaying of Gray iamge
cv2.imshow('Gray image', gray)
#Saving of image
cv2.imwrite("gray_scale.png",gray)
cv2.waitKey(0)#wait for the key event
cv2.destroyAllWindows()
