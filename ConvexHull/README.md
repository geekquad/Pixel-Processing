# <b>Convex Hull in OpenCV</b>

## What is convex hull?
- A Convex object is one with no interior angles greater than 180 degrees. 
- Hull means the exterior or the shape of the object. 
- Hence, onvex Hull of a shape or a group of points is a tight fitting convex boundary around the points or the shape.

## Convex Hull in OpenCV:
- We can find convex hull in opencv by firstly making the image binary and finding the contours in the image.
- Convex hull in OpenCV can be obatined with the help of the following method

```
    cv2.convexHull()
```

## Actual image:

![Image](https://i.imgur.com/n3zs6ts.jpg)

## Images with contours and convex hulls

Here blue lines show the convex hull for the yellow contours

![Image](https://i.imgur.com/PKL3FEM.jpg)

## Author
[Rohini Rao](https://github.com/RohiniRG)