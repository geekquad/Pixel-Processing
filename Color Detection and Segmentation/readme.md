# Color Detection and Segmentation

This repository contain study and implementation of color detection technique and then segmentation of the detected color.

## Detection of a color

Color detection algorithms are used to indentify pixels in an image that match a specified color or color range.

Suppose we have a RGB image (Red-Green-Blue) and it is tempting to simply threshold the color channel and get our mask (an ndarray of 1s and 0s). It turns out that this will not work effectively since the RGB values are highly sensitive to illumination. For example even though for red color there might be some areas where, due to shadow, red channel values of the corresponding pixels can be quite low. 

The right approach turned out to transform the color space of our image from RGB to HSV (Hue–Saturation–Value). In HSV space, colors are much more localized and visually separable. The saturation and value of the colors do vary, but they are mostly located within a small range along the hue axis. This is the key point that can be leveraged for segmentation.

## Image segmentation

In computer vision, image segmentation is the process of partitioning a digital image into multiple segments (sets of pixels, also known as image objects). The goal of segmentation is to simplify and/or change the representation of an image into something that is more meaningful and easier to analyze.

Using the detected color space we can create a binary mask (an ndarray of 1s and 0s), where values of 1 indicate values within the range, and zero values indicate values outside, and then use these masks to filter out different segments from the image. The color space detected can be used to perform object segmentation in images. This segmentation technique is simple, fast, and reliable.

## Instructions for use

1. Install Python 3x and pip.

2. Install virtual environment and create a new environment
    - ```$ pip install virtualenv && virtualenv venv```

3. Install dependencies
    - ```$ pip install -r requirements.txt```

4. Run
    - ```$ py/python/python3 ./color_detection_and_segmentation/cloak.py```

    
