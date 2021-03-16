# Change of color spaces basically means changing the representation of an array of pixel color.

import cv2 as cv

img = cv.imread('images/henry.jpg')

# for higher pixel images it is a better practice to resize the img or each frame of the video 
def rescaleImg(frame,scale=0.25): # set scale accordingly 
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)
    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)

img =  rescaleImg(img)
cv.imshow('Img',img)

# BGR to Gray Scale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)
cv.waitKey(0)