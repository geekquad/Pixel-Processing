# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 01:19:57 2020

@author: Chandrika PC
"""


import cv2
import numpy as np
face_cascade=cv2.CascadeClassifier(r"C:\Users\Chandrika PC\OneDrive\Pictures\Saved Pictures\haarcascade_frontalface_default.xml")
img=cv2.imread("C:/Users/Chandrika PC/OneDrive/Pictures/Saved Pictures/kerdeshian sisters.jpg")
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#determine the coordinates of the face
faces=face_cascade.detectMultiScale(img_gray, scaleFactor=1.2,minNeighbors=5)
print(type(faces))
print(faces)

for x,y,w,h in faces:
    img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
    cv2.putText(img,"Face",(x,y),cv2.FONT_HERSHEY_SIMPLEX,0.6,(255,255,0),2)

    cv2.imshow("image",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
  
                       
