# FAST Algorithm for Corner Detection

There are several feature-detetcting algorithms, which work really well. But when looking from a real-time application point of view, they are not fast enough.
As a solution to this, FAST (Features from Accelerated Segment Test) algorithm was proposed by *Edward Rosten and Tom Drummond* in the year 2006 in their paper “Machine learning for high-speed corner detection” .

## Feature Detection using FAST

![image](https://opencv-python-tutroals.readthedocs.io/en/latest/_images/fast_speedtest.jpg)

**12 point segment test corner detection in an image patch**

The highlighted squares are the pixels used in the corner detection. The pixel at p is the center of a candidate corner. The arc is indicated by the dashed line passes through 12 contiguous pixels which are brighter than p by more than the threshold.

Although it is several times faster than other existing corner detectors, still it is not robust to high levels of noise.
It is dependant on a threshold.

## FAST Feature Detector in OpenCV

It is called in the same way as any other feature detector in OpenCV. One can specify the threshold, whether non-maximum suppression to be applied or not, the neighborhood to be used or not, etc.

For the neighborhood, three flags are defined,<br/>
cv2.FAST_FEATURE_DETECTOR_TYPE_5_8<br/>
cv2.FAST_FEATURE_DETECTOR_TYPE_7_12<br/>
cv2.FAST_FEATURE_DETECTOR_TYPE_9_16<br/>

**References:**

>[opencv-python-tutorials](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_feature2d/py_fast/py_fast.html)

>[medium](https://medium.com/data-breach/introduction-to-fast-features-from-accelerated-segment-test-4ed33dde6d65)
