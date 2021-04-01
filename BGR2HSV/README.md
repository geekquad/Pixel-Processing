
<![endif]-->

# Change Color Space


## Goal[](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_colorspaces/py_colorspaces.html#goal "Permalink to this headline")

> -   In this tutorial, you will learn how to convert images from one color-space to another, like BGR  ![\leftrightarrow](https://opencv-python-tutroals.readthedocs.io/en/latest/_images/math/41a61df92c33a32be9fd6375536739eca63f43ab.png)  Gray, BGR  ![\leftrightarrow](https://opencv-python-tutroals.readthedocs.io/en/latest/_images/math/41a61df92c33a32be9fd6375536739eca63f43ab.png)  HSV etc.
> -   In addition to that, we will create an application which extracts a colored object in a video
> -   You will learn following functions :  **cv2.cvtColor()**,  **cv2.inRange()**  etc.
## # Changing Color space


There are more than 150 color-space conversion methods available in OpenCV. But we will look into only two which are most widely used ones, BGR  ![\leftrightarrow](https://opencv-python-tutroals.readthedocs.io/en/latest/_images/math/41a61df92c33a32be9fd6375536739eca63f43ab.png)  Gray and BGR  ![\leftrightarrow](https://opencv-python-tutroals.readthedocs.io/en/latest/_images/math/41a61df92c33a32be9fd6375536739eca63f43ab.png)  HSV.

For color conversion, we use the function  `cv2.cvtColor(input_image,  flag)`  where  `flag`  determines the type of conversion.

For BGR  ![\rightarrow](https://opencv-python-tutroals.readthedocs.io/en/latest/_images/math/a9c4c6156d25f42923975ce449aadad9848ed7dc.png)  Gray conversion we use the flags  `cv2.COLOR_BGR2GRAY`. Similarly for BGR  ![\rightarrow](https://opencv-python-tutroals.readthedocs.io/en/latest/_images/math/a9c4c6156d25f42923975ce449aadad9848ed7dc.png)  HSV, we use the flag  `cv2.COLOR_BGR2HSV`. To get other flags, just run following commands in your Python terminal
>>> import cv2
>>> flags = [i for i in dir(cv2) if i.startswith('COLOR_')]
>>> print flags

## How to Use

1. Run the notebook file 
(webcam starts)
2. Three new windows opens showcasing the outputs

    
