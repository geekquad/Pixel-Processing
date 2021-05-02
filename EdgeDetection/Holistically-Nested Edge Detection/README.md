# Holistically-Nested Edge Detection

Edge detection enables us to find the boundaries of objects in images and was one of the first applied use cases of image processing and computer vision.

When it comes to edge detection with OpenCV everyone most likely utilize the Canny edge detector; however, there are a few problems with the Canny edge detector, namely:

* Setting the lower and upper values to the hysteresis thresholding is a manual process which requires experimentation and visual validation.
* Hysteresis thresholding values that work well for one image may not work well for another (this is nearly always true for images captured in varying lighting conditions).
* The Canny edge detector often requires a number of preprocessing steps (i.e. conversion to grayscale, blurring/smoothing, etc.) in order to obtain a good edge map.

Holistically-Nested Edge Detection (HED) attempts to address the limitations of the Canny edge detector through an end-to-end deep neural network.

This network accepts an RGB image as an input and then produces an edge map as an output. Furthermore, the edge map produced by HED does a better job preserving object boundaries in the image.

The HED model requires 2 files, namely :

* **deploy.prototxt** which is a python dict-like wrapper class to process google protobuf objects. adequately describe the network architecture.
* **hed_pretrained_bsds.caffemodel** which simply define the internal states of the parameters/gradients of the layers.


### Result

<img src="https://github.com/KKhushhalR2405/Image-Processing-OpenCV/blob/hed/EdgeDetection/Holistically-Nested%20Edge%20Detection/out.jpg" width="700" height="300">
