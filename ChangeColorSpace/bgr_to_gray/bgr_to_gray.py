import cv2

org_img = cv2.imread("jahangir.jpg")
cv2.imshow("bgr_image",org_img)


mod_img = cv2.cvtColor(org_img,cv2.COLOR_BGR2GRAY)
cv2.imshow("gray_image",mod_img)
k = cv2.waitKey(0) & 0xFF

if k == 27:  #press esc to exit
     cv2.destroyAllWindows()







