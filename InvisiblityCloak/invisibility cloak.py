import cv2
import numpy as np
import time


cap = cv2.VideoCapture(0)
time.sleep(2)
background = 0

#captured the background here
for i in range(30):
    ret, background = cap.read()


while (cap.isOpened()):
    ret, img = cap.read()
    
    if not ret:
        break
        
    hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
    
    lower_red = np.array([0,120,70])#HSV values
    upper_red = np.array([10,255,255])#HSV values
    mask1 = cv2.inRange(hsv, lower_red, upper_red) #seperating the cloak part

    lower_red = np.array([170,120,70])#HSV values
    upper_red = np.array([180,255,255])#HSV values
    mask2 = cv2.inRange(hsv, lower_red, upper_red) #seperating the cloak part
    
    mask1 = mask1 + mask2
    
    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, np.ones((3,3), np.uint8), iterations = 2 ) #Noice Removal
    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_DILATE, np.ones((3,3), np.uint8), iterations = 2) #Noice Removal
    
    mask2 = cv2.bitwise_not(mask1)#everything except the cloak
    
    res1 = cv2.bitwise_and(background, background , mask = mask1) #Used for the segmentaion of the colors
    res2 = cv2.bitwise_and(img , img , mask = mask2)#used to substitute the cloak part 
    final_output = cv2.addWeighted(res1, 1, res2, 1,0)
    cv2.imshow("Eurekaa  !!!", final_output)
    k = cv2.waitKey(10)
    if k == 27:
        break
cap.ralease()
cv2.destroyAllWindows()    