# Affine Transformation 


## Introduction<br>

* In Affine transformation, all parallel lines in the original image will still be parallel in the output image.<br>
### How to find Affine transformation:-
* To find the transformation matrix, we need three points from input image and their corresponding locations in the output image. Then cv2.getAffineTransform will create a 2×3 matrix which is to be passed to cv2.warpAffine.<br>
* Affine transformation uses angle of rotation that is clockwise which is in contrast to the typical geometry unit circle of angles being measured in counter clockwise rotation with 0 starting from the positive X axis, therefore you will see that the negative of the angle is often applied.<br>
### Example Code:-
```import cv2
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread('food.jpeg')
rows, cols, ch = img.shape

pts1 = np.float32([[50, 50],
				[200, 50],
				[50, 200]])

pts2 = np.float32([[10, 100],
				[200, 50],
				[100, 250]])

M = cv2.getAffineTransform(pts1, pts2)
dst = cv2.warpAffine(img, M, (cols, rows))

plt.subplot(121)
plt.imshow(img)
plt.title('Input')

plt.subplot(122)
plt.imshow(dst)
plt.title('Output')

plt.show()

# Displaying the image
while(1):
	
	cv2.imshow('image', img)
	if cv2.waitKey(20) & 0xFF == 27:
		break
		
cv2.destroyAllWindows()
 ```
 ### Output
 ![image](https://user-images.githubusercontent.com/74819092/119949672-b914ca80-bfb7-11eb-8986-06e86680e411.png)


<p align="center">
</p>


### How Algorithms Works? <br>
* We mentioned that an Affine Transformation is basically a relation between two images. The information about this relation can come, roughly, in two ways:<br>
                      - We know both X and T and we also know that they are related. Then our task is to find M <br>
                      - We know M and X. To obtain T we only need to apply T=M⋅X. Our information for M may be explicit (i.e. have the 2-by-3 matrix) or it can come as a                                  geometric relation between points.<br>
* Let's explain this in a better way (b). Since M relates 2 images, we can analyze the simplest case in which it relates three points in both images. Look at the figure below:

<p align="center">
  
  ![image](https://user-images.githubusercontent.com/74819092/119952482-b1a2f080-bfba-11eb-8f46-9cfdfd5a0854.png)
  
</p>

<br>
the points 1, 2 and 3 (forming a triangle in image 1) are mapped into image 2, still forming a triangle, but now they have changed notoriously. If we find the Affine Transformation with these 3 points (you can choose them as you like), then we can apply this found relation to all the pixels in an image.



### Advantages<br>

### Disadvantages<br>


### Applications <br>
* Affine transformation is a linear mapping method that preserves points, straight lines, and planes. Sets of parallel lines remain parallel after an affine transformation. The affine transformation technique is typically used to correct for geometric distortions or deformations that occur with non-ideal camera angles.<br>
* Affine Transformation helps to modify the geometric structure of the image, preserving parallelism of lines but not the lengths and angles. It preserves collinearity and ratios of distances.<br>
* This technique is also used to correct Geometric Distortions and Deformations that occur with non-ideal camera angles.<br>


### References <br>
* https://stackabuse.com/affine-image-transformations-in-python-with-numpy-pillow-and-opencv/<br>
* https://medium.com/mlait/affine-transformation-image-processing-in-tensorflow-part-1-df96256928a<br>
* https://docs.opencv.org/3.4/d4/d61/tutorial_warp_affine.html<br>
* https://mathworld.wolfram.com/AffineTransformation.html#:~:text=An%20affine%20transformation%20is%20any,remains%20the%20midpoint%20after%20transformation).<br>
