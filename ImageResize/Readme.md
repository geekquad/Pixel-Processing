
# Image Rotation

Image Rotation is deployed by using cv2.rotate() method. It can be used to rotate the image by the given angle and clockwise or anticlockwise manner,depending upon our need.
# Image Scaling

Image Scaling is deployed using cv2.resize() method. It can be used to scale up or scale down a given image in x or y axis, depending upon our need.

# Image Zooming

For this, first the width and height of the output image is calculated ,based upon the amount of zoooming required to be applied.
Then ,cv2.resize() method is deployed to finally zooom the given image.

This function Resize the images.
# Image Translation

Translation refers to the rectilinear shift of an object i.e. an image from one location to another.
cv2.wrapAffine() function has been used here,to implement the translation.
