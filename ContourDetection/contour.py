# import cv2 module
import cv2 


def contourDetection(image):

    # Image is converted to gray-scale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # We can only apply thresholding to gray_scale images

    # cv2.threshold(source_image, thresh_value, max_value, threshold_type, destination=None)
    # thresh_value can be adjusted according to the image
    _ , thresh = cv2.threshold(gray_image, 205, 255, 0) 
    
    # contours are detected using the below function
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # function returns the array containing the coordinates of the contours
    return contours
    

def displayImageWithContours(image,contours):

        # All contours will be displayed if index is set to -1
        index = -1 
        
        # thickness is set
        thickness = 2

        # color of the contour is set to blue(BGR)
        color = (255,0,0)

        # contours are drawn on the original image with the help of the below function
        cv2.drawContours(image, contours, index, color, thickness)

        # cv2.imshow displays the image
        cv2.imshow("Contours",image)


if __name__ == "__main__":
    # main code starts here

    # path to image 
    # 1 indicates to load the image in color
    image = cv2.imread('images/demo1.png', 1)

    # contourDetection() is called to detect contours
    contours = contourDetection(image)

    # function to display contours is called
    displayImageWithContours(image, contours)

    # waits indefinitely 
    cv2.waitKey()

    # destroys all the windows created
    cv2.destroyAllWindows()
