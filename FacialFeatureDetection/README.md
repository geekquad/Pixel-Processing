# Facial Feature Detection

## About Project
In this project, I am making use dlib library and OpenCV to mimic the facial filters like Snapchat or Instagram. In today's time, facial filters have garnered immense popularity amongst the millennials and Gen-Z alike. 

Currently, the project supports basic filter props such as moustache, funny eyes and santa claus. But the possibilities of different facial filters are endless.

## Implementation

I have used pretrained weights to predict the facial landmarks of the person(s) on the live webcam. Dlib library is used to load these weights and make the prediction. 

Please refer to the picture below for the different facial landmarks that can be predicted using ```shape_predictor_68_face_landmarks.dat``` file.

![img](https://camo.githubusercontent.com/04da00a85d1bb8f8aaeca0da27cccad8d63674896f8b858d60759bb3af98d25e/68747470733a2f2f63646e2d696d616765732d312e6d656469756d2e636f6d2f6d61782f313630302f312a393655542d44387553586a6c6e79767339445a546f672e706e67)

Once the landmarks are identified, I am using OpenCV to load the filter props, resize them based on the size of face and then, superimpose them over the live-streaming frame for filter like effect.

Filter to be applied is selected using function argument.