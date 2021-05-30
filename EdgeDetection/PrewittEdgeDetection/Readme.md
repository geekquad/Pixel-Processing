# Prewitt Edge Detection


## Introduction<br>

* Prewitt operator is used for edge detection in an image. It detects two types of edges. Horizontal edges. Vertical Edges.<br>

<p align="center">

<img src="https://user-images.githubusercontent.com/74819092/120063273-f21a7100-c083-11eb-8545-048e844f7a6d.png" width=400, height=400>
<img src="https://user-images.githubusercontent.com/74819092/120063279-fcd50600-c083-11eb-9d7e-a1eb0319db65.png" width=400, height=400>

</p>



### How Algorithms Works? <br>
* Edges are calculated by using difference between corresponding pixel intensities of an image. All the masks that are used for edge detection are also known as derivative masks. Because as we have stated many times before in this series of tutorials that image is also a signal so changes in a signal can only be calculated using differentiation. So that’s why these operators are also called as derivative operators or derivative masks.

* All the derivative masks should have the following properties:
              - Opposite sign should be present in the mask.
              - Sum of mask should be equal to zero.
              - More weight means more edge detection.
Step 1: Input – Read an image<br>
Step 2: Convert the true-color RGB image to the grayscale image<br>
Step 3: Convert the image to double<br>
Step 4: Pre-allocate the filtered_image matrix with zeros<br>
Step 5: Define Prewitt Operator Mask<br>
Step 6: Edge Detection Process (Compute Gradient approximation and magnitude of vector)<br>
Step 7: Display the filtered image<br>
Step 8: Thresholding on the filtered image<br>
Step 9: Display the edge-detected image
  <br>
(For more details regarding Stages check first Refrence link )

### Advantages<br>
*  Good performance on detecting vertical and horizontal edges.
*  Best operator to detect the orientation of an image.
### Disadvantages<br>
* The magnitude of coefficient is fixed and cannot be changed.
* Diagonal direction points are not preserved always.



### Applications <br>
* it is a discrete differentiation operator, computing an approximation of the gradient of the image intensity function.<br>
* Widely used in Computer Vision. <br>
* main application of edge detection is in detecting objects in an image.<br>


### References <br>
* https://www.tutorialspoint.com/dip/prewitt_operator.htm<br>
* https://www.geeksforgeeks.org/matlab-image-edge-detection-using-prewitt-operator-from-scratch/ <br>
* https://medium.com/@nikatsanka/comparing-edge-detection-methods-638a2919476e<br>
* https://www.youtube.com/watch?v=EDNS2UYG-0I<br>
