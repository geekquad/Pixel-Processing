## Facial Landmarks Detection using Dlib and Open-CV

Sometimes simply the face detection isn't enough and a lot of programs require various operations to be performed on various parts of the facial region. Here we perform the detection of facial landmarks in realtime (using a pre trained detector provided by Yin Guobing). I have also added the Helen dataset and the 5 point detector just in case. There are many more pre-trained models you can possibly try.

![img](https://github.com/akshitadixit/Image-Processing-OpenCV/blob/master/FacialLandmarkDetection/Assets/mapping.png)

Create a virtual environment for python>3.6 and install the following if already not done.

> conda install -c conda-forge dlib

> conda install -c conda-forge opencv-python

Alternatively you can also install the above by using pip install dlib, opencv-python

Then simply run imagedetection.py for images and videodetection.py for real-time landmark detection.
