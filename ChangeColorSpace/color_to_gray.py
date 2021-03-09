from PIL import Image, ImageOps 
#Enter the path 
path=input("Enter the path : ")
#Open the image 
im1 = Image.open(path) 
#Convert the color image to Gray Scale 
im2 = ImageOps.grayscale(im1) 
 #Display the image
im2.show()
#Save the image in the desired location
im2.save("gray_image.png")
