# Erosion

1.Erodes away the boundaries of foreground object.
2.Used to diminish the features of an image.

# Working of Erosion.

1.A kernel(a matrix of odd size(3,5,7) is convolved with the image.
  Here, matrix of size=5 has been used.
2.A pixel in the original image (either 1 or 0) will be considered 1 only if all the pixels under the kernel is 1, otherwise it is eroded (made to zero).
3.Thus all the pixels near boundary will be discarded depending upon the size of kernel.

Hence, the thickness or size of the foreground object decreases or simply white region decreases in the image.