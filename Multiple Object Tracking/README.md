# Multiple Object Tracking using OpenCV 
It aims at the tracking of multiple objects in motion from a video. Basically, a video is a collection of frames, and if we want to know the position of multiple objects
in a frame captured from a video then we require bounding boxes and trackers. The OpenCV library of Python will help us to attain our result as it mainly focuses on 
image processing, video capturing, and analysis like object detection and object tracking.

### Multiple Object Tracker in OpenCV: 
There are several trackers in OpenCV, for example- a correlation-object tracker, boosting tracker, MIL tracker, csrt tracker, etc. But the MultiTracker Class in OpenCV 
provides an implementation of multiple-object tracking using multiple trackers.

#### It requires two inputs: 
1. video frame 2. bounding boxes of all objects to be tracked

##### Syntax: trackers = _cv2.MultiTracker_create()_

The steps involved to create this project are:

1) import OpenCV

2) Create a dictionary of all the trackers and access the MultiTracker class for tracking operation.

3) Give the path of the video stream, read and capture frames from that.

4) To track k number of objects, initialise a variable k.

5) Now select the region of interest (ROI) i.e create a rectangle over the objects which we call as bounding boxes.

6) The rectangle consists of four coordinates (x,y,w,h), x is the x coordinate of the topmost corner, y is the y coordinate of the topmost corner, w is the width and 
h is the height.

7) Add all the trackers, this function will allow us to add trackers with all objects.

8) loop over the frames and update it until false is returned by the compiler.

9) Now release video stream and destroy all windows.
