# Optical Flow 

## What is optical flow ?
Optical flow or optic flow is the pattern of apparent motion of objects, surfaces, and edges in a visual scene caused by the relative motion between an observer and a scene. Optical flow can also be defined as the distribution of apparent velocities of movement of brightness pattern in an image.
<br/>

## Methods
- ### Lucas-Kanade method.
- ### Dense optical flow method.

<br/><br/>
# Lucas-Kanade Method:

- Lucas–Kanade method is a widely used differential method for optical flow estimation.
- It assumes that the flow is essentially constant in a local neighbourhood of the pixel under consideration, and solves the basic optical flow equations for all the pixels in that neighbourhood, by the least squares criterion.
- By combining information from several nearby pixels, the Lucas–Kanade method can often resolve the inherent ambiguity of the optical flow equation.
- It is also less sensitive to image noise than point-wise methods. On the other hand, since it is a purely local method, it cannot provide flow information in the interior of uniform regions of the image.
<br/>

## Lucas-Kanade Algorithm in Opencv:
Python's opencv provides a method to implement Lucas-Kanade algorithm for our convenience which can be used as follows

```sh 
    cv2.calcOpticalFlowPyrLK() 
```

## Output of Lucas-Kanade Algorithm
![gif](https://media.giphy.com/media/IuisYtbi66crmPaN9l/giphy.gif)

<br/><br/>
# Dense optical flow method:

- Lucas-Kanade method computes optical flow for a sparse feature set. OpenCV provides another algorithm to find the dense optical flow. 
- Dense Optical flow computes the optical flow vector for every pixel of the frame which may be responsible for its slow speed but leading to a better accurate result. 
- It can be used for detecting motion in the videos, video segmentation, learning structure from motion. There can be various kinds of implementations of dense optical flow. 
<br/>

## Dense optical flow method in Opencv:
Python's opencv provides a method to implement Dense optical flow algorithm for our convenience which can be used as follows

```sh 
    cv2.calcOpticalFlowFarneback() 
```

## Output of Dense optical flow  Algorithm
![gif](https://media.giphy.com/media/AUWKosGOmzMRs7cleS/giphy.gif)

<br/>

# Author
[Akhil Bhalerao](https://github.com/iamakkkhil)