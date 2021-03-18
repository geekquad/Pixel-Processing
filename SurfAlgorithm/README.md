# SURF (Speeded-Up Robust Features) Algorithm

SURF algorithm is a patented local feature detector and descriptor used for tasks like Object Recognition, Image Registration, Image Classification and 3D Reconstruction. The main advantage of SURF is the fast computation of operators using box filters. Instead of Gaussian averaging the image, squares are used for approximation since the convolution with sqaure is much faster if the integral image is used.


## SURF is composed of 2 steps
**1. Feature Extraction**

**2. Feature Description**

## Procedure
- SURF approximates the LoG with Box Filter. Below image shows this approximation. One big advantage of this approximation is that, convolution with box filter can be easily calculated with the help of integral images. 

<p align="center">
  <img width="300" height="300" src="https://i.postimg.cc/prFhm53j/SURF1.png">
</p>

- The above can be done parallel for different scales. SURF relies on determinant of Hessian matrix for both the scale and location.
- For orientation assignment, SURF uses wavelet responses in horizontal and vertical direction for a neighbourhood of size 6s. Adequate guassian weights are also applied to it.
-  The dominant orientation is estimated by calculating the sum of all responses within a sliding orientation window of angle 60 degrees. 

<p align="center">
  <img width="300" height="300" src="https://i.postimg.cc/SN5mDLgF/SURF2.png">
</p>


-  SURF also provides such a functionality called Upright-SURF or U-SURF.
-  For feature description, SURF uses Wavelet responses in horizontal and vertical direction (again, use of integral images makes things easier)
-  A neighbourhood of size 20sX20s is taken around the keypoint where s is the size. It is divided into 4x4 subregions. 
-  For each subregion, horizontal and vertical wavelet responses are taken and a vector is formed like this, **V = (∑ dx, ∑ dy, ∑|dx|, ∑|dy|)**

- This when represented as a vector gives SURF feature descriptor with total 64 dimensions. Lower the dimension, higher the speed of computation and matching, but provide better distinctiveness of features.

## Referenes
- [Introduction to SURF - openCV](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_feature2d/py_surf_intro/py_surf_intro.html)
- [Introduction to SURF - Medium](https://medium.com/data-breach/introduction-to-surf-speeded-up-robust-features-c7396d6e7c4e)
- [Comparision of SIFT, SURF and ORB - Medium](https://medium.com/@shehan.a.perera/a-comparison-of-sift-surf-and-orb-333d64bcaaea)