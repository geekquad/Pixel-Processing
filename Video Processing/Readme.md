## Video Processing using OpenCV
* Code is present in `Video Processing.ipynb`.
* You can simply download and execute it in jupyter notebook.
* One sample video is also added in folder named video.
    
### Overview 
1. Function `getVideoFrames` is developed to read desired number of frames from video.
2. Uses inbuilt function of Opencv like VideoCapture for reading the video file.
3. Then `isOpened()` is used to check if video opened or not.
4. To find a given number of frames from video, we will use fps and total frame count to detect the desired frames from all frames.  
5. Information like frames per second(fps), frame count etc are stored in flags cv2.CAP_PROP_FPS and cv2.CAP_PROP_FRAME_COUNT in cv2.
6. Then for each desired frame, the flag `CAP_PROP_POS_FRAMES` is set with the frame to read next using `set(1 , frameNumber-1)` and then read the frame.
7. Then frames are resized using `cv2.resize` and appended to the list.
8. Finally, this function will return the desired frames from video.
 
### Function `getVideoFrames`
  * Input Parameters:
    * video - path of the video 
    * frameWidth - resize frame to this width
    * frameHeight - resize frame to this height
    * numOfFrames - total number of frames we want to extract
    
  * Output:
    * Returns list of frames 
    
### Use Cases
This method can be used to apply all the algorithms implemented on images to videos.  
