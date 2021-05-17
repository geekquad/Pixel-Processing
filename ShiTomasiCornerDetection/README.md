# Shi Tomasi Corner Detection and Good Features to Track


## What is a corner?
A corner can be interpreted as the junction of two edges (where an edge is a sudden change in image brightness).


## Shi-Tomasi Corner Detector:
In 1994, J. Shi and C. Tomasi made a small modification to it in their paper Good Features to Track which shows better results compared to Harris Corner Detector. 
The scoring function in Harris Corner Detector was given by:

(where λ1, λ2 are eigenvalues of resultant matrix)

    R = λ1λ2 - k(λ1 + λ2)
 
Instead of this, Shi-Tomasi proposed:

    R = min(λ1, λ2)   

Only when λ1 and λ2 are above a minimum value, λmin , it is considered as a corner.


## OpenCV's Good Features to Track:
cv2.goodFeaturesToTrack() finds N strongest corners in the image by Shi-Tomasi method. 

![Image](https://i.imgur.com/Cyu3ba3.png)


## Author
[Rohini Rao](https://github.com/RohiniRG)

