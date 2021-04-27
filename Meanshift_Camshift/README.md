# FACE TRACKING USING MEAN-SHIFT AND CAM-SHIFT ALGORITHM

## What is FACE TRACKING?
Face Tracking is a <b>Computer Vision</b> technology that detects and locates the presence of a human face in a digital image or video. The technology is anonymous and only discerns a human face by focusing on facial features, providing information about a person’s gender and age bracket.

</br>

## MeanShift Algorithm?
- Meanshift is a very useful method to keep track of a particular object inside a video.
- We define an initial window, generally a square or a circle for which the positions are specified by ourself which identifies the area of maximum pixel distribution and tries to keep track of that area in the video. 
- The direction of movement depends upon the difference between the center of our tracking window and the centroid of all the k-pixels inside that window.

</br>

- MeanShift algorithm can be used in <b>OpenCV</b> as follows :
```sh 
    cv2.meanShift()
```

</br>

## CamShift Algorithm?
- It is an enhanced version of the meanshift algorithm which provides more accuracy and robustness to the model. 
- With the help of Camshift algorithm, the size of the window keeps updating when the tracking window tries to converge.
- Also, it provides the best fitting tracking window for object tracking.

</br>

- CamShift algorithm can be used in <b>OpenCV</b> as follows :
```sh 
    cv2.CamShift()
```


</br>

## Output:

### Meanshift Algorithm working: 
![GIF](https://media.giphy.com/media/UuQNG8anZ5XRCQMgTA/giphy.gif)

### Camshift Algorithm working:
![GIF](https://media.giphy.com/media/FmC6S9475vIqkbeOg7/giphy.gif)


</br>

## Author
[Akhil Bhalerao](https://github.com/iamakkkhil)
