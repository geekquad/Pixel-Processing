Face Detection in Images

Face and Eye detection is done using Haar Cascade. Haar Cascade is a
Machine Learning based approach where a cascade function is trained
with set of input data.It contains pre-trained classifiers for face,
eyes,smile etc. For face detection we have used a face classifier
and similarly for eye detection we have used an eye classifier.
Using Opencv we can detect faces and eyes in images as well as videos.

Step-1:Import all the necessary libraries like opencv.

Step-2:Add the path of classifier(pre-trained) for face detection
as face_cascade.

Step-3:Using the function imread() , we can add the path of any image
we want.

Step-4: Using rectangle() function a rectangle is created around our face

Step-5:Using imshow() function,we can display output image