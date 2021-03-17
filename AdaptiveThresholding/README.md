# Adaptive Thresholding Method
---

### Thresholding
---
Thresholding is the binarization of an image. We convert a grayscale image to a binary image, where the pixels are either 0 or 255. 


### Simple Thresholding
A simple thresholding is selecting a pixel value x, and then selecting all pixel intensities less than x to zero, and all pixel values greater than x to 255. In this way, we are able to create a binary representation of the image. We use thresholding to focus on objects or areas in an image. 

### Adaptive Thresholding
AS in simple thresholding we have to manually supply our threshold value T, which require a lot of manual experiments and parameter tunings. Just one value of T might not be enough. Adaptive threshold considers a small neighbors of pixels and then finds an optimal threshold value T for each neighbor. This can help in cases where there may be ranges of pixel intensities and the optimal value T may change for different parts of the image.


