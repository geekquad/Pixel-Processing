# GRAB-CUT ALGORITHM FOR BACKGROUND SUBTRACTION

## What is Background Subtraction?
<b>Background Subtraction</b> or <b>Foreground Extraction</b> is any technique which allows an image’s background to be removed or foreground to be extracted for further processing like object recognition, tracking, etc. 


## Grab-cut Algorithm?
- In this algorithm, the region is drawn in accordance with the foreground required.
- A rectangle is drawn over it. This is the rectangle that encases our main object. 
- The region coordinates are decided over understanding the foreground maska and segmentation can be done more accurately by manual coordinate selection.
- This technique functions similar to a green screen in cinematics.


## Grab-cut Algorithm in Opencv:
Python's opencv provides a method to implement Grab-Cut algorithm for our convenience which can be used as follows

```sh 
    cv2.grabCut()
```

## Output:

### Input image is:

![Image](https://i.imgur.com/5CtcU7L.jpg)

### After applying grabcut algorithm:

![Image](https://i.imgur.com/jJMA2Sd.jpg)


## Author
[Akhil Bhalerao](https://github.com/iamakkkhil)

