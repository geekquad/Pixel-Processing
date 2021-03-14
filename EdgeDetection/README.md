# Edge Detection

Implementation of the following Edge Detection methods:

* Canny Edge Detection  

* Robert Edge Detection :         
    The idea behind the Roberts operator is to approximate the gradient of an image through discrete differentiation which is achieved by computing the sum of the squares of the differences between diagonally adjacent pixels.       
    ```
    So, the Robert Mask kernels are : 
    Rx = [[ 1,  0],
           0, -1]]
    Ry = [[ 0,  1], 
          [-1,  0]]
    ```
    The explaination can be found [here](https://en.wikipedia.org/wiki/Roberts_cross). 

    Original image      |  Robert Edge Detected         
    :-------------------------:|:-------------------------:     
    <img width="350" height="350" src="https://github.com/Bhumika-Kothwal/Image-Processing-OpenCV/blob/edge-detection/EdgeDetection/Robert_EdgeDetection_img.jpg">|<img width="350" height="350" src="https://github.com/Bhumika-Kothwal/Image-Processing-OpenCV/blob/edge-detection/EdgeDetection/Robert_EdgeDetection_output.jpg">
* Prewitt Edge Detection
* Sobel Edge Detection
