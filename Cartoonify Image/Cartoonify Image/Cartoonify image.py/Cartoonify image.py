import cv2                           #importing cv library
import numpy as np                   #importing numpy library as np                      

path = input("Enter the path of image\n") 
img = cv2.imread(path)                            #to read an image
img = cv2.resize(img,(540,540))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)      #cv2.COLOR_BGR2GRAY is used for BGR Gray conversion.
gray = cv2.medianBlur(gray, 5)                    #used for smoothening the image
cv2.imshow("Gray", gray)                          #used to show the image after BGR to Gray Conversion
edges = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,9,9)   #used when image has different lighting conditions in different areas. It calculate the threshold for a small regions of the image. 

#cartoonize
color = cv2.bilateralFilter(img, 9, 250, 250)                 #used for smoothening images and reducing noise
cv2.imshow("filtered", color)                                 #used for showing the image after applying filters
cartoon = cv2.bitwise_and(color, color, mask = edges)         #applying bitwise operation 'and' which invert the color 


cv2.imshow("Original", img)                #used to show the image.
cv2.imshow("Cartoon", cartoon)             #used to show the cartoonified image


cv2.waitKey(0)            #it is a keyboard binding function              
cv2.destroyAllWindows()   #destroys all the windows                                                                                       
                                                                                                                                      
