# <b>Bitwise Operations in OpenCV</b>

- Bitwise operations in opencv include AND, OR, NOT, and XOR operations.

- They are highly useful while extracting any part of the image, defining and working with non-rectangular ROI's, generating masks from the image, etc.

## Bitwise AND Operation:
- Here pixel value is set to True if and only if both pixels are greater than zero.
- We implement this in openCV using
```
    cv2.bitwise_and()
```

### Example

| Shape 1 | Shape 2 | Result |
|---------|---------|--------|
|![Image](https://i.imgur.com/sH8fSj0.png)         |![Image](https://i.imgur.com/lQ80pHI.png)         |![Image](https://i.imgur.com/t0oyEGz.png)        |

#

## Bitwise OR Operation:
- Here pixel value is set to True if either of the two pixels is greater than zero.
- We implement this in openCV using
```
    cv2.bitwise_or()
```

### Example

| Shape 1 | Shape 2 | Result |
|---------|---------|--------|
|![Image](https://i.imgur.com/sH8fSj0.png)         |![Image](https://i.imgur.com/lQ80pHI.png)         |![Image](https://i.imgur.com/djdbiy6.png)        |

#

## Bitwise XOR Operation:
- Here pixel value is set to True is set to True if and only if one of the two pixels is greater than zero, but not both.
- We implement this in openCV using
```
    cv2.bitwise_xor()
```

### Example

| Shape 1 | Shape 2 | Result |
|---------|---------|--------|
|![Image](https://i.imgur.com/sH8fSj0.png)         |![Image](https://i.imgur.com/lQ80pHI.png)         |![Image](https://i.imgur.com/GjmCIao.png)        |

#

## Bitwise NOT Operation:
- Here pixel values are inverted.
- We implement this in openCV using
```
    cv2.bitwise_not()
```

### Example

| Shape | Result |
|---------|---------|
|![Image](https://i.imgur.com/sH8fSj0.png)         |![Image](https://i.imgur.com/vLvSpat.png)         |
