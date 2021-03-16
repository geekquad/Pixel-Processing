import cv2
import numpy as np

def Harris_Corner_Detector(path):
    pic = cv2.imread(img_path)
    pic_gray = cv2.cvtColor(pic,cv2.COLOR_BGR2GRAY)

    pic_arr = np.float32(pic_gray)
    #print(pic_arr)
    dst = cv2.cornerHarris(pic_arr,3,5,0.02)
    dst = cv2.dilate(dst,None)

    pic[dst>0.02*dst.max()]=[255,0,0]
    return(pic)

if __name__=="__main__":
    img_path = 'image.jpg'
    pic = Harris_Corner_Detector(img_path)
    cv2.imshow('Cor',pic)
    if cv2.waitKey(0) & 0xff == 27:
        cv2.destroyAllWindows()
