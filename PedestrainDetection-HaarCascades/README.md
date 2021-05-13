# Pedestrain Detection using HaarCascades

__HaarCascades__ , It is an Object Detection Algorithm used to identify faces in an image or a real time video. The algorithm uses edge or line detection features. It is given a lot of positive images consisting of faces, and a lot of negative images not consisting of any face to train on them.

* Positive Images : These images contain the images which we want our classifier to identify.

* Negative Images : Images of everything else, which do not contain the object we want to detect.

The model created from this training is available at the OpenCV GitHub repository:

https://github.com/opencv/opencv/tree/master/data/haarcascades

The repository has the models stored in XML files, and can be read with the OpenCV methods. These include models for face detection, eye detection, upper body,lower body detection,full body detection, license plate detection etc.

## Pedestrain Detection a.k.a. Full Body Detection using HaarCascades

>Libraries used : numpy, OpenCV, time

_Step 1 :_ In order to detect the features  of a full-body we need to import the  [haarcascade_fullbody.xml](https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_fullbody.xml) .

_Step 2 :_ Read the image or video using __cv2.imread()__ and __cv2.VideoCapture()__ respectively and store them in a variable say "cap".

_Step 3 (for video input) :_ Loop inside the video using __cap.isOpened__ . Reading (cap.read()) from a VideoCapture returns a tuple (ret, frame). Where __"ret"__ will obtain return value from getting the camera frame, either true of false and "frame" will get the next frame in the camera (via "cap").

_Step 4 :_ Now that we have the tuple of (ret, frame) , we will convert the BGR channel image to gray channel. Reasons being the same, we are converting the image to gray scale and using the classifier function detectMultiScale to extract the x-coordinate, y-coordinate, width (w) and height(h), and gray scale is used for better performance throughput.

_Step 5 :_ Based on the extracted features/dimensions of the cars, we will loop through them and draw a rectangle around each frame of the image.

_Step 6 :_ Display the result.

Although haarcascade classifier is pretty helpful, there are few drawbacks of this approach.

1. The most challenging part of this is accurately specifying the parameter value of scaleFactor and minNeighbors of the detectMultiScale function. It is pretty common to run into scenarios where we need to tune both the parameters on a image-by-image basis which is a big turn off when it comes to an image detection use-case.

2. The scaleFactor is basically used to control the image pyramid which in turn is used to detect the object at various scales of an image. If the scaleFactor is too large then chances are that the image detection will not be accurate and we will be missing objects at scales that fall in between the pyramid layers.

3. However, if we decrease the value of scaleFactor then you will get many layers of pyramids on the same image scale which makes detection slower and increases false-positives.






