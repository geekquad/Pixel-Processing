# Watershed Algorithm

## About Watershed Algorithnm
Watershed algorithm takes image as an input. Algorithm would treat the intensity value of each pixel in the image as its height.
So, the brighter the pixel, the height it is. Each object in the image must have a low intensity, picking again in terms of height it means that each object must be a "basin".
So, for example:- if we have 10 basins means 10 objects in the image. The point of contact of different objects is marked as a ridge line. (Ridge Line = edge of a object)

## Requirement for the Watershed Algorithm
1. Each object in the image must be a "Basin".
2. The center of each object should be near the bottom of the basin.

## Steps for Performing Watershed Transformation
1. Segment objects of interest and generate a mask.
2. Convert the mask into an intensity profile using the Distance Transformation(Computes distance between each pixel and nearest non-zero pixel).
3. Run the Watershed Algorithm.
4. update the original mask.

## Original Image

![coins](https://user-images.githubusercontent.com/57597700/113509357-c17df580-9572-11eb-89e7-401aa13511c0.jpg)

## Resultant Image

![Resultant_image](https://user-images.githubusercontent.com/57597700/113510583-305e4d00-9579-11eb-9f15-9c0af83e6de1.jpg)


