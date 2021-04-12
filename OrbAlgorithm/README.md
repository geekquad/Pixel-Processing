# ORB (Oriented FAST and Rotated BRIEF)

This algorithm was brought up by Ethan Rublee, Vincent Rabaud, Kurt Konolige and Gary R. Bradski in their paper [*ORB: An efficient alternative to SIFT or SURF in 2011*](http://www.willowgarage.com/sites/default/files/orb_final.pdf). It is a good alternative to SIFT and SURF in computation cost, matching performance and mainly the patents.

ORB is basically a fusion of FAST keypoint detector and BRIEF descriptor with many modifications to enhance the performance.

* First it uses FAST to find keypoints,
* Then it applies Harris corner measure to find top N points among them.<p>
It also use pyramid to produce multiscale-features.


## How Fast(Features from Accelerated and Segments Test) is used in ORB:
--------------

Given a pixel p in an array fast compares the brightness of p to surrounding 16 pixels that are in a small circle around p. These pixels are then sorted into three classes (lighter than p, darker than p or similar to p). If more than 8 pixels are darker or brighter than p than it is selected as a keypoint. Keypoints found by fast gives us information of the location of determining edges in an image.

![FAST](https://miro.medium.com/max/554/0*CZ2Ub21iuBOgpMDb.jpg)

However, FAST features do not have an orientation component and multiscale features. So it uses a multiscale image pyramid. Once orb has created a pyramid it uses the fast algorithm to detect keypoints in the image. By detecting keypoints at each level orb is effectively locating key points at a different scale. In this way, ORB is partial scale invariant.

![FAST_ORIENTATION](https://miro.medium.com/max/375/0*wGPpgnPImtwLb8NX.png)

## How Brief(Binary robust independent elementary feature) is used in ORB:
-----------------

Brief takes all keypoints found by the fast algorithm and converts it into a binary feature vector so that together they can represent an object.

![BRIEF](https://miro.medium.com/max/875/1*8v4ZvgwE0DYiCzQDRvno1A.png)

The matching performance of BRIEF falls off sharply for in-plane rotation of more than a few degrees. ORB proposes a method to steer BRIEF according to the orientation of the keypoints.

rBRIEF shows significant improvement in the variance and correlation over steered BRIEF.

## ORB in OpenCV
---------------
In OpenCv, we have to create an ORB object with the function, cv2.ORB() or using feature2d common interface. It has a number of optional parameters, out of which the most useful ones are nFeatures, scoretypes, etc.

* nFeatures denotes maximum number of features to be retained (by default 500)
* scoreType denotes whether Harris score or FAST score to rank the features (by default, Harris score) etc.
* WTA_K decides number of points that produce each element of the oriented BRIEF descriptor.
By default it is two, ie selects two points at a time.
In that case, for matching, NORM_HAMMING distance is used.
If WTA_K is 3 or 4, which takes 3 or 4 points to produce BRIEF descriptor, then matching distance is defined by NORM_HAMMING2.

**References:**

>[OpenCv Docs](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_feature2d/py_orb/py_orb.html)

>[Medium](https://medium.com/data-breach/introduction-to-orb-oriented-fast-and-rotated-brief-4220e8ec40cf)
