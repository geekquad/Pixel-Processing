# Bilateral Filtering

A bilateral filter is used for smoothening images and reducing noise, while preserving edges.Similarly to the Gaussian convolution, the bilateral filter is also defined as a weighted average of pixels. We know that a Gaussian filter takes the a neighborhood around the pixel and finds its Gaussian weighted average. This Gaussian filter is a function of space alone, that is, nearby pixels are considered while filtering. It does not consider whether pixels have almost the same intensity value and does not consider whether the pixel lies on an edge or not. The resulting effect is that Gaussian filters tend to blur edges, which is undesirable.

The bilateral filter also uses a Gaussian filter in the space domain, but it also uses one more (multiplicative) Gaussian filter component which is a function of pixel intensity differences. The Gaussian function of space makes sure that only pixels are ‘spatial neighbors’ are considered for filtering, while the Gaussian component applied in the intensity domain (a Gaussian function of intensity differences) ensures that only those pixels with intensities similar to that of the central pixel (‘intensity neighbors’) are included to compute the blurred intensity value. As a result, this method preserves edges, since for pixels lying near edges, neighboring pixels placed on the other side of the edge, and therefore exhibiting large intensity variations when compared to the central pixel, will not be included for blurring.
## Mathematically

Gaussian blurring can be formulated as follows:

![](https://media.geeksforgeeks.org/wp-content/uploads/20190824233655/gaussian_eq.png)

Here, GB[I]p is the result at pixel p, and the RHS is essentially a sum over all pixels q weighted by the Gaussian function. Iq is the intensity at pixel q.

## Bilateral Filter: an Additional Edge Term

The bilateral filter can be formulated as follows:
</br>

![](https://media.geeksforgeeks.org/wp-content/uploads/20190825010814/Untitled-Diagram-138.png)

Here, the normalization factor and the range weight are new terms added to the previous equation. σs denotes the spatial extent of the kernel, i.e. the size of the neighbourhood, and σr denotes the minimum amplitude of an edge. It ensures that only those pixels with intensity values similar to that of the central pixel are considered for blurring, while sharp intensity changes are maintained.

## Parameters:

The bilateral filter is controlled by two parameters: σs and σr. 

* As the range parameter σr increases, the bilateral filter becomes closer to Gaussian blur
because the range Gaussian is flatter i.e., almost a constant over the intensity interval
covered by the image.
* Increasing the spatial parameter σs smooths larger features.

An important characteristic of bilateral filtering is that the weights are multiplied, which
implies that as soon as one of the weight is close to 0, no smoothing occurs. As an example,
a large spatial Gaussian coupled with narrow range Gaussian achieves a limited smoothing
although the filter has large spatial extent. The range weight enforces a strict preservation of
the contours.


</br>
</br>

![](images/img2.jpg)
> Example of result obtained with the Bilateral filter. First columns shown the original image (top) and the smoothed image (bottom). Second column is a zoom on one partof the image (top) with corresponding level lines below. Third column is the same illustrationbut for the result.

</br>
</br>


![](images/img1.jpg)
>The bilateral filter smooths an input image while preserving its edges. Each pixel is replaced by a weighted average of its neighbors. Each neighbor is weighted by a spatial component that penalizes distant pixels and range component that penalizes pixels with a different intensity. The combination of both components ensures that only nearby similar pixels contribute to the final result. The weights are represented for the central pixel (under the arrow).

In Image Processing using python bilateral filtering can be applied using two libraries: __skimage__ & __opencv__.

Here, I have used opencv in which __cv2.bilateralFilter()__ is used to perform the operation. It is highly effective at noise removal while preserving edges but the operation is slower compared to other filters.

It is defined as :
>cv2.bilateralFilter(	src, d, sigmaColor, sigmaSpace, dst[, borderType]]	)

where :

* __d__ : Diameter of each pixel neighborhood.
* __sigmaColor__ : Value of __sigma__ in the color space. The greater the value, the colors farther to each other will start to get mixed.
* __sigmaSpace__ : Value of __sigma__ in the coordinate space. The greater its value, the more further pixels will mix together, given that their colors lie within the sigmaColor range.
* __dst__ : Destination image of the same size and type as src .
* __borderType__ : Border mode used to extrapolate pixels outside of the image.

## Comparison with other filters

### __Noisy Image__

</br>

![](https://media.geeksforgeeks.org/wp-content/uploads/20190825194611/taj.jpg)

</br>



<table>
  <tr>
    <td>Gaussian filter</td>
     <td>Median filter</td>
     <td>Bilateral Filter</td>
  </tr>
  <tr>
    <td><img src="images/1.jpg" width=800 height=300></td>
    <td><img src="images/2.jpg" width=800 height=300></td>
    <td><img src="images/3.jpg" width=800 height=300></td>
  </tr>
 </table>

 </br>
 </br>

 * Bilateral Filter is slow in processing than other filters