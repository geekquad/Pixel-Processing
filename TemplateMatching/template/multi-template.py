########################## yasmeen mohammed sharaan (YMMSSH) ######################
##########################            GSSoC'21               ######################
##########################         Multiple -template           ######################


#import libraries
import cv2
import numpy as np
from matplotlib import pyplot as plt


######### first templete #########
#import images 
img_rgb = cv2.imread('test_images//baby.jpg')
template = cv2.imread('test_images//tie.png',0)

img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY) #convert the image which is required to find the object on  to gray
w, h = template.shape[::-1] #store rows and columns of the image of the object

#apply templete matching
res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where( res >= threshold)

#ehwn you find the object draw rectangle around it
for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)



######### first templete #########
#### the same code but in another images for confirmation

img2_rgb = cv2.imread('test_images//multi-template.png')
img2_gray = cv2.cvtColor(img2_rgb, cv2.COLOR_BGR2GRAY)
template2 = cv2.imread('test_images//multi-template-coin.png',0)
w, h = template2.shape[::-1]

res2 = cv2.matchTemplate(img2_gray,template2,cv2.TM_CCOEFF_NORMED)
threshold = 0.8
loc2 = np.where( res2 >= threshold)

for pt in zip(*loc2[::-1]):
    cv2.rectangle(img2_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)

    
cv2.imshow('res',img_rgb)
cv2.imshow('res2',img2_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()
