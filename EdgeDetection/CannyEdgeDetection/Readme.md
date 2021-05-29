# Affine Transformation 


## Introduction<br>

* It is a multi-stage algorithm and we will go through each stages.to detect a wide range of edges in images.<br>


<p align="center">
  
  <img src="https://user-images.githubusercontent.com/74819092/120062455-05c3d880-c080-11eb-862f-d6f434e9b24b.png" height=400, width=700>

</p>


### How Algorithms Works? <br>
*  Noise Reduction
*  Finding Intensity Gradient of the Image
*  Non-maximum Suppression
*  Hysteresis Thresholding
  <br>
(For more details regarding Stages check first Refrence link )

### Advantages<br>
*  The presence of Gaussian filter allows removing of any noise in an image.
*  The signal can be enhanced with respect to the noise ratio by non-maxima suppression method which results in one pixel wide ridges as the output.
*  Detects the edges in a noisy state by applying the thresholding method.
* The effectiveness can be adjusted by using parameters.
*  It gives a good localization, response and is immune to a noisy environment.
### Disadvantages<br>
* The primary disadvantage of using Canny edge detector is that it consumes a lot of time due to its complex computation.
* It is difficult to implement to reach the real-time response.
* If the amount of smoothing required is important in the spatial domain it may be slow to compute.
*  It gives a bias towards vertical and horizontal edges and does not give a good approximation of rotational symmetry.



### Applications <br>
* Technique to extract useful structural information from different vision objects and dramatically reduce the amount of data to be processed.<br>
* Widely used in Computer Vision. <br>
* It is used to detect spontaneous, contractions.<br>


### References <br>
* https://docs.opencv.org/master/da/d22/tutorial_py_canny.html<br>
* https://en.wikipedia.org/wiki/Canny_edge_detector <br>
* https://towardsdatascience.com/canny-edge-detection-step-by-step-in-python-computer-vision-b49c3a2d8123<br>
* https://www.youtube.com/watch?v=17cOHpSaqi0<br>
