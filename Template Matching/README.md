# <b>Template Matching in OpenCV</b>

- Template Matching is a method for searching and finding the location of a template image in a larger image.
- It is one of the simplest forms of object detection, where a template is basically slided over the reference image to find if there is a match.
- OpenCV provides a function to find matches, known as

```
    cv2.matchTemplate()
```

## Reference image
![Image](https://i.imgur.com/Lhwk3RM.jpg)

## Template image
![Image](https://i.imgur.com/62zVGzn.jpg)

## Comaparison of different template matching methods

- OpenCV offers various types of methods that aid in template matching, their working can be observed as follows

| Method | Template Matching |
|---------|---------|
| cv2.TM_CCOEFF |![Image](https://i.imgur.com/Ut4PB9O.png)|
| cv2.TM_CCOEFF_NORMED | ![Image](https://i.imgur.com/tbThQSA.png)|
| cv2.TM_CCORR | ![Image](https://i.imgur.com/tcghzNp.png)|
| cv2.TM_CCORR_NORMED | ![Image](https://i.imgur.com/VWCzkj5.png)|
| cv2.TM_SQDIFF | ![Image](https://i.imgur.com/qiR1JMp.png)|
| cv2.TM_SQDIFF_NORMED | ![Image](https://i.imgur.com/IcF9sBh.png)|

- Among the above mentioned methods, we can clearly say that `cv2.TM_CCORR` doesn't provide an accurate match


## Author
[Rohini Rao](https://github.com/RohiniRG)

