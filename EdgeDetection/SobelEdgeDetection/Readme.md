# Sobel Edge Detection


## Introduction<br>

* The Sobel operator performs a 2-D spatial gradient measurement on an image and so emphasizes regions of high spatial frequency that correspond to edges.
*  Typically it is used to find the approximate absolute gradient magnitude at each point in an input grayscale image.<br>


<p align="center">

<img  src="https://user-images.githubusercontent.com/74819092/120098264-7f2bfb80-c152-11eb-8138-7fecc537897c.png" height="400">

</p>


### How Algorithms Works? <br>
*  It works by calculating the gradient of image intensity at each pixel within the image. It finds the direction of the largest increase from
light to dark and the rate of change in that direction.
* The result shows how abruptly or smoothly the image changes at eachpixel, and therefore how likely it is that that pixel represents an edge.
* It also shows how that edge is likely to be oriented.
* The result of applying the filter to a pixel in a region of constant intensity is a zero vector.
* The result of applying it to a pixel on an edge is a vector that point sacross the edge from darker to brighter values

### Advantages<br>
*  Sobel operator finds more edges or make edges more visible as compared to Prewitt Operator. 
This is because in sobel operator we have allotted more weight to the pixel intensities around the edges.
*  The primary advantages of the Sobel operator lie in its simplicity.
*  Sobel method provides a approximation to the gradient magnitude.
*  The Sobel-Feldman operator is a separable edge detection filter.

### Disadvantages<br>
* It cannot produce smooth and thin edge compared to canny method.
* It is difficult to implement to reach the real-time response.
* If the amount of smoothing required is important in the spatial domain it may be slow to compute.
* The major disadvantage of Sobel operator was the signal to noise ratio.



### Applications <br>
* used in image processing, particularly within edge detection algorithms where it creates an image emphasising edges..<br>
* Widely used in Computer Vision. <br>


### References <br>
* https://www.cs.auckland.ac.nz/compsci373s1c/PatricesLectures/Edge%20detection-Sobel_2up.pdf<br>
* https://homepages.inf.ed.ac.uk/rbf/HIPR2/sobel.htm
* https://www.tutorialspoint.com/dip/sobel_operator.htm
* https://www.youtube.com/watch?v=uihBwtPIBxM

