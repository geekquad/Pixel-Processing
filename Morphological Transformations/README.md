## Morphological Transformations
### Morphological transformations are some simple operations based on the image shape. It is normally performed on binary images. It needs two inputs, one is our original image, second one is called structuring element or kernel which decides the nature of operation. Two basic morphological operators are Erosion and Dilation.

## Erosion 
- It erodes away the boundaries of the foreground object and removes small-scale details from an image but simultaneously reduces the size of regions of interest.
- OpenCV Erosion : cv2.erode()

## Dilation
- It erodes away the boundaries of the foreground object and removes small-scale details from an image but simultaneously reduces the size of regions of interest.
- OpenCV Dilation : cv2.dilate()

## Opening
- Opening is a process in which first erosion operation is performed and then dilation operation is performed.
- Opening is used for removing internal noise of the obtained image.
- Open CV opening : cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
## Closing 
- Closing is a process in which first dilation operation is performed and then erosion operation is performed.
- Closing CV opening : cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
## Morphological Gradients
- It is the difference between dilation and erosion of an image.
- The result will look like the outline of the object.
## Top Hat
- It is the difference between input image and Opening of the image. 
## Black Hat
- It is the difference between the closing of the input image and input image.