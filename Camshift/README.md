# Camshift Algorithm

__Continuously adaptive mean-shift__ (CAMShift) is an efficient and light-weight tracking algorithm developed based on mean-shift. __Mean-shift__ is a kernel-based tracking method which uses
density-based appearance models to represent targets. The
method tracks targets by finding the most similar distribution
pattern in a frame sequences with its sample pattern by iterative
searching. It has been widely used because of its relative
simplicity and low computational cost, but mean-shift would
fail in changing the track window`s scale, as targets move
toward or away from the camera.

Based on mean-shift, _continuous adaptive mean-shift_
( CAMShift ) was proposed to overcome the problem.
CAMShift adaptively adjusts the track window's size and the
distribution pattern of targets during tracking. CAMShift
algorithm can be used to track the distribution of any kind of
feature that represents the target in a lightweight, robust and
efficient way. Most researchers though, use color data to
represent targets for CAMShift, this would give a low
complexity and practical performance to the method.

While CAMShift performs well with objects that have a
simple and constant appearance, it is not robust in more
complex scenes. For example, when background has similar
color distribution with a target, or when a target moves in front
of different color background objects, the tracker is very likely
to fail. In another case, when the initial search window contains
some parts of the background, due to poor object detection, it
would normally cause the CAMShift`s search window to drift
and diverge. This might be an intense problem because the
traditional CAMShift algorithm usually starts with manually
selecting a target region by a user , and a human user may
not be able to fully segment the target region form the
background. The problem of search window drift is inherent to
many probability-based trackers, since these techniques only
track the peak of a probability distribution – not taking into
account the composition of probabilities.

## Whats' & Whys' of the Code

For better understanding I have divided the code into different sections.

## __Section 1__

>Importing the required libraries: numpy , cv2

Defining three global variables that we’ll be using throughout the rest of this script.

_frame_ : which is the current frame of the video that we are processing.

_roiPts_ : which is the list of points corresponding to the __Region of Interest__ (ROI) in our video.

_inputMode_ : which is simply used as a boolean flag, indicating whether or not we are currently selecting the object we want to track in the video.

## __Section 2 ( selectROI function )__



Referencing to our current frame, list of ROI points, and input mode indicator.

Then we make a check for three conditions. In order to select the ROI, these three
conditions must hold:

1.  We are currently in input mode (which allows us to select the ROI of the object we want to
track in the video).

2. The left button of the mouse was clicked, as indicated by the _cv2.EVENT_LBUTTONDOWN_ constant, giving us the (x, y) coordinates of the click.

3. We must have less than four points currently in our list of ROI points. In this example, we’ll
assume that our ROI can be representing as a bounding box with four points.

Assuming that these conditions hold, we then append the (x, y) location of the click to our list of ROI points , draw a circle representing the location of the mouse click on , and then display the updated frame.

Using this selectROI function we will be able to select the object that we want to track in our video.


## __Section 3 (main function )__

We capture the Live video from our webcam using _cv2.VideoCapture_ in a variable _camera_.

Now we to have to select the bounding box of the object we want to track in our video and in order to do this, we’ll need to register an event callback. We do this by creating a window named _frame_ and indicating that any mouse events applied to the _frame_ window should be handled by our _selectROI_ function.

Finally, we initialize a tuple containing our termination criteria for the CamShift algorithm.The CamShift algorithm is iterative, meaning that it seeks to optimize the tracking criterion. In this case, we’ll set the termination criterion to perform two checks.

* The first check is the epsilon associated with the centroids of our selected ROI and the tracked ROI
according to the CamShift algorithm. If the tracked centroid has not changed by at least one pixel,
then terminate the CamShift algorithm.

* The second check controls the number of iterations of CamShift. Using more iterations will allow
CamShift to (ideally) find a closer centroid match between the selected ROI and the tracked ROI;
however, this comes at the cost of runtime. If the iterations are set too high, then we will drop below
real-time performance, which is substantially less than ideal in most situations. And so we use a maximum of 10 iterations so we don’t fall into this scenario.

## __Section 4 ( Examining frames of the video )__

We start looping over the frames by grabbing the current frame.

The call to _camera.read()_ returns a tuple with two values. The first _grabbed_ , indicates whether or not reading the frame was a success. The second is the _frame_ itself. We now make a check to see if the frame was successfully grabbed if not, then we make the assumption that we are at the end of the video and we break from the loop.

We then checks to see if we have selected a bounding box for our object to track yet.

Provided that we have selected a bounding box, the first thing we’ll do is convert our image from the
RGB color space to the HSV color space and compute the histogram back projection on, using only the Hue component of the color space.

Once we have the back projection, we apply the CamShift algorithm on by making a call to _cv2.CamShift_.This function expects three arguments:

*  _backProj_ : Which is the output of the histogram back projection.

* _roiBox_ : The estimated bounding box containing the object that we want to track.

* _termination_ : Our termination criterion.

The _cv2.CamShift_ function then returns two values to us. The first contains the estimated position,
size, and orientation of the object we want to track. We then take this estimation and draw a rotated
bounding box.

Finally, the second output of the cv2.CamShift function is the newly estimated position of the ROI,
which will be re-fed into subsequent calls into the cv2.CamShift function.


## __Section 5 ( setting the input ROI & creating the reference histogram )__

Primarily we display the current frame on screen & then check if a key is pressed.

If the _" i "_ key was pressed and there are less than four points in our list of points corresponding to
the ROI, then we drop down into input mode.

From there, we set _inputMode = True_ to indicate that we are selecting our ROI. We also make a clone of the original frame.This freezes the frame on display, waiting for the bounding box of 4 points to be selected.

After we have our bounding box, we convert our ROI points to a NumPy array, and grab the top-left
and bottom-right points, respectively.

Given the top-left and bottom-right points, we then grab the ROI from the original frame and convert
it from the RGB to the HSV color space.

In order to apply the cv2.CamShift function, we need the output of the back projection. And the
only way to obtain the back projection is to create a reference histogram of the object we want to
track.

We then construct this histogram by making a call to _cv2.calcHist_ and the normalizing it. Again, we are only using the Hue component of the HSV color space.

It is important to note the 4th parameter of _cv2.calcHist_ — the number of bins. In this case, we are using only 16 bins in the histogram. In OpenCV, hue values can fall within the range [0, 180], so tuning the number of bins for your application will certainly be important.

Finally, we construct the ROI bounding box using the top-left and bottom-right points, respectively.

In order to break out of our frame loop, we’ll also monitor if the _" q "_ key is pressed. If the _" q "_ key is pressed, we’ll break out of the loop.

We then release the reference to our camera and close all open windows.


## Running the Code

* After running the code, the webcam window appears showing the Live Stream. 

* Press " _i_ " to take the input and mark four points on the boundary of the object you want to track making a rectangular frame. 

* After that press any key on to exit Input mode andd you could see your object being tracked by a rectangular frame around it.

* To exit or break the Live stream press " _q_ ".

__Note :__ Avoid selecting those images whose colour matches your background. Since the tracking takes place through histogram matching from the frame it might track any object whose colour matches your selected object.










