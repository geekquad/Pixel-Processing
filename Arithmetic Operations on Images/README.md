# Arithmetic Operations on Images
We can carry out arithmetic operations like adding and subtracting images using OpenCV Python.

### Requirement
_pip install opencv-python_

## Addition of Images 
We can add two images using the function **cv2.addWeighted()**.  
It takes 5 arguments image1, image2, weight of image1, weight of image2 and light value of final image. 

<img src="cosmic1.jpg" width="350" height="250" />            <img src="nature.jpg" width="350" height="250" />

The final output image after addition is:  

 <img src="FinalAdd.png" width="350" height="250" />

## Subtraction of Images
To subtract two images, use the function **cv2.subtract(image1,image2)**.  

<img src="circle1.jpg" width="350" height="250" />                <img src="pattern1.jpg" width="350" height="250" />

The final Output image obtained after subtracting is:  

 <img src="FinalSub.png" width="350" height="250" />


