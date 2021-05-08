# <b>Feature Matching and Homography</b>

## What is Feature Matching?

- In image processing, the distinct feature points of images help us to compare and detect objects in images or videos.
- OpenCV provides algorithms like BruteForce Matcher and FLANN based Matcher, and detectors like SIFT and SURF algorithms to help with this process.
- In this script we are using <b>FLANN based matcher (Fast Library for Approximate Nearest Neighbors) paired with SIFT feature detectors</b>. FLANN contains a collection of algorithms optimized for fast nearest neighbor search.

## What is Homography?

- Homography is a transformation that maps the points in one point to the corresponding point in another image.
- In simple words, it helps to recognize familiar features of an object from an image and detects the object when places in a complex scene.

## Reference object

![Image](https://i.imgur.com/JuC0r5o.jpg)

## Complex scene containing similar object

![Image](https://i.imgur.com/59rlIVs.jpg)

## Object Detection using Feature Matching and Homography

![Image](https://i.imgur.com/2uUUHyc.jpg)

## Author
[Rohini Rao](https://github.com/RohiniRG)