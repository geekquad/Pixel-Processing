# Depth Map

A minimal implementation of creating Depth Map or Disparity Map.

> Depth information means the distance of surface of scene objects from a viewpoint.
> The disparity of a pixel is equal to the shift value that leads to minimum sum-of-squared-differences for that pixel.

Because of the difference in the images our eyes receive, being at a distance from each other, we get a depth intuition and can tell how far away objects are. This is called stereo vision. We will call the two images that make up a single view, **a stereo pair**. Here the stereo pair chosen is as follows:

![right](assets\right.jpg)   ![left](assets\left.jpg)

And the disparity or depth-map produced is as follows:

![ss](assets\screenshot.png)

Better results can be achieved by tuning the parameters numDisparities and blockSize.

