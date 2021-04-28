# Brute Force Matcher

Brute Force Feature matching is simply comparing the keypoint descriptors of one image to other. The features of an image include its corners, edges or its other parts. It compares the features based on some type of distance calculation like the hamming distance and then returns the one with closest match.

## Implementation of Brute Force Feature Matching

* Feature Detection: The first thing to be done is to detect the features in images to compare using methods like SIFT, SURF, ORB etc.


* cv2.BfMatcher(): It creates the BFMatcher object. It takes two optional parameters:
  * normType: It specifies the distance measurement to be used. The default value is cv2.NORM_L2. We also have cv2.NORM_L1. It is used for feature detectors like SURF, SIFT etc. For BRIEF, ORB, BRISK etc cv2.NORM_HAMMING is used that makes the use of hamming distance for calculations. For ORB if VTA_K is 3 or 4 we use cv2.NORM_HAMMING2.  
  * crossCheck: It is a boolean variable which is false by default. It returns the best matches betwen sets A and B only if they are same i.e. for a match (i, j) it returns the match only if the ith descriptor of set A is same as the jth descriptor of set B. It gives consistent result.


* BFMatcher.match() and BFMatcher.knnMatch() : BFMatcher.match() returns the best matches. BFMatcher.knnMatch() returns the k best matches. The BFMatcher.match() returns a list of DMatch objects which have the following attributes:
  * DMatch.distance: distance between the descriptors.
  * DMatch.trainIdx: index of descriptor in train descriptors.
  * DMatch.queryidx: index of descriptor in quer descriptors.
  * Dmatch.imgIdx: index of the train image.


* cv2.drawMatches(): It stacks the two images to compare and draw the lines from one image to the other showing the matched features. We also have cv2.drawMatchesKnn which draws the k best matches. For k equals 2 two lines would be drawn for each keypoint descriptor.  

## Source
https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_feature2d/py_matcher/py_matcher.html
