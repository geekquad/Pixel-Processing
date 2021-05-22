# Arithmetic Operations on Images
We can carry out arithmetic operations like adding and subtracting images using OpenCV Python.

### Requirement
_pip install opencv-python_

## Addition of Images 
We can add two images using the function **cv2.addWeighted()**.  
It takes 5 arguments image1, image2, weight of image1, weight of image2 and light value of final image. 

<img src="Images/cosmic1.jpg" width="350" height="250" />            <img src="Images/nature.jpg" width="350" height="250" />

The final output image after addition is:  

 <img src="Images/FinalAdd.png" width="350" height="250" />

## Subtraction of Images
To subtract two images, use the function **cv2.subtract(image1,image2)**.  

<img src="Images/circle1.jpg" width="350" height="250" />                <img src="Images/pattern1.jpg" width="350" height="250" />

The final Output image obtained after subtracting is:  

 <img src="Images/FinalSub.png" width="350" height="250" />


