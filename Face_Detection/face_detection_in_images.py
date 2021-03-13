import cv2
face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
a=cv2.imread("image.png")
g=cv2.cvtColor(a,cv2.COLOR_BGR2GRAY)
faces=face_cascade.detectMultiScale(g,1.05,5)
for (x,y,w,h) in faces:
    a=cv2.rectangle(a,(x,y),(x+w,y+h),(0,255,0),3)
s=cv2.resize(a,(500,500))
cv2.imshow('F',s)
cv2.waitKey(0)
cv2.destroyAllWindows()