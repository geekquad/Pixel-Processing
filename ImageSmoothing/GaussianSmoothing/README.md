# Gaussian Filter

Gaussian Filter also referred to as "Gaussian Blur" is a filter that is used in image processing for de-noising or removing noises form an input image. It can also be said that it basically blurs the image by using the "Gaussian Function".

It is a widely used effect in graphics software, typically to reduce image noise and reduce detail. The visual effect of this blurring technique is a smooth blur resembling that of viewing the image through a translucent screen, distinctly different from the bokeh effect produced by an out-of-focus lens or the shadow of an object under usual illumination. It is also one of the filters available in photoshop used for blurring.


![Bokeh effect created by Gaussian Filter](https://images.unsplash.com/photo-1485288734756-0b31a0a31d95?ixid=MXwxMjA3fDB8MHxzZWFyY2h8OHx8Ymx1cnJlZHxlbnwwfHwwfA%3D%3D&ixlib=rb-1.2.1&w=1000&q=80)
>Bokeh effect created by Gaussian Filter


The mathematics behind Gaussian Filter is convolving the image with the **Gaussian Function** which also expresses the _normal distribution_ in statistics. This function is used for calculating the transformation which is applied on each pixel of the image by convolving the image with a kernel of a particular size and sigma.

The one-dimensional function is expressed as 

![](https://wikimedia.org/api/rest_v1/media/math/render/svg/dd16b16869269dba008d19c0969515a1d50b3ae2)

The two-dimensional Gaussian function is expressed as 

![](https://wikimedia.org/api/rest_v1/media/math/render/svg/6717136818f2166eba2db0cfc915d732add9c64f)

where x is the distance from the origin in the horizontal axis, y is the distance from the origin in the vertical axis, and σ is the standard deviation of the Gaussian distribution. When applied in two dimensions, this formula produces a surface whose contours are concentric circles with a Gaussian distribution from the center point.

**Graphically they are expressed as below**

![](https://www.researchgate.net/profile/Kazumi-Suematsu/publication/342883563/figure/fig5/AS:912626649399296@1594598557124/One-dimensional-end-to-end-distance-distributions-averaged-out-for-the-octamer-N-8-g.png)
>One-dimensional graph 


![](https://www.mathworks.com/help/examples/stats/win64/ComputeTheMultivariateNormalPdfExample_01.png)
>Two-dimensional graph

In python ,Gaussian Kernel is defined either by Kernel size or sigma.
Here I have used **OpenCv** which is defined by Kernel-Size whereas in **skimage** sigma is used in Gaussian Filter.

![](https://i.stack.imgur.com/Qc4Mq.gif)
>Example of kernel of sigma=1

![](https://i.stack.imgur.com/CQiM7.png)
> Kernel with small sigma and large sigma respectively


Here I have used three ways for Gaussian-Filtering an image:

* cv2.GaussianBlur (the pre-defined function for blurring)
* cv2.getGaussianKernel (defining the kernel according to our need)
* Creating a Gaussian Function of our own