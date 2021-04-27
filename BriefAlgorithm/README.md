# BRIEF Algorithm (Binary Robust Independent Elementary Features)

The BRIEF algorithms provides a shortcut to find the binary strings directly without finding descriptors.



It takes smoothened image *patch* and selects a set of n_d (x,y) location pairs in an unique way. After that, some pixel intensity comparisons are done on these location pairs.<p>
For eg, let first location pairs be p and q. If I(p) < I(q), then its result is 1, else it is 0. This is applied for all the n_d location pairs to get a n_d-dimensional bitstring.

*The defined neighborhood around pixel(keypoint) is known as a patch, which is a square of some pixel width and height.*
![patch](https://miro.medium.com/max/875/1*lZ1sloEeHwZ3tXw4InCZJw.png)

Selecting a set of n_d (x,y) location pairs can be done using one of five approaches(Sampling Geometries) given below:

![BREIF_G1](https://miro.medium.com/max/781/0*bTfQfO4qOxk3qL78) <p>

  Now this n_d can be 128, 256 or 512. OpenCV supports all of these (in bytes 16, 32, 64), but by default, it would be 256. Once we get this, we can use Hamming Distance to match these descriptors.

![BRIEF_bin_features_vector](https://miro.medium.com/proxy/1*XWpgdt4Z4xeT-g8hn5JLsA.png)

One important point is that BRIEF is a feature descriptor, it doesn’t provide any method to find the features.<p>
One will have to use any other feature detectors like SIFT, SURF etc to do the job.
  
Brief relies on a relatively small number of intensity diﬀerence tests to represent an image patch as a binary string. Not only is construction and matching for this descriptor much faster than for other state-of-the-art ones, but it also tends to yield higher recognition rates, as long as invariance to large in-plane rotations is not a requirement.

In short,<p>
BRIEF is a faster method feature descriptor calculation and matching.<p>
It also provides high recognition rate unless there is large in-plane rotation.
  
  
**Resources**
> [OpenCV](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_feature2d/py_brief/py_brief.html)

> [Medium](https://medium.com/data-breach/introduction-to-brief-binary-robust-independent-elementary-features-436f4a31a0e6)
