**_**Marking Attendance using FACE RECOGNITION**_**


In this project we will figure out how to perform Facial recognition with high precision and will make an Attendance project that will utilize webcam to recognize faces and record the attendance live in a excel sheet which will include the name, date and time.


**_This Project consists of 6 simple steps :_**
1. Import Libraries.
2. Load images.
3. Convert into RGB & Find Encodings.
4. Run Webcam.
5. Match Images.
6. Mark Attendance.


**LET’S START**


**_1. Importing the required Libraries._**
First we will import the relevant Libraries. We have to import all the necessary libraries into the code. “cv2” is for OpenCV, “face_recognition” is for recognition related operations and “numpy” is for the numerical purposes.


**_2. Loading Images._**
The Face Recognition package consists of a load image function that loads the images from the destination source/path provided.


![image](https://user-images.githubusercontent.com/74240933/113142245-4b168600-9248-11eb-9f67-332e0e3e4f23.png)


**_3. Converting into RGB and find Encodings._**
Once the image is imported now it’s time to convert the image into RGB, because we are getting the images as BGR but library understands it as RGB.


![image](https://user-images.githubusercontent.com/74240933/113142326-5ff31980-9248-11eb-9ccb-c3976a0c7c84.png)


After converting the image now it’s time to find the image encodings by using face_encodings() function. It is basically comparing these image face and finding the distance between them. We have the encoding of both the images now we just are going to compare these encodings.


**_4. Run webcam and find it’s Encodings._**

**RUN WEBCAM**


**READ WEBCAM IMAGE AND RESIZE**
Now we will read the image from webcam and will resize it to make the program fast, it will help us to reduce the data.


**WEBCAM IMAGE ENCODINGS**


![image](https://user-images.githubusercontent.com/74240933/113142037-11de1600-9248-11eb-80cf-d5aee5d7206e.png)


And once we have our perfect webcam frame then we will be finding faces in our image. face_locations() is used to perform this task.


**_5. Match the images._**
Now it’s the time to match current face encodings with our images list encodings in order to find the best match.

![image](https://user-images.githubusercontent.com/74240933/113142067-1dc9d800-9248-11eb-8c83-d47458f5a804.png)

In order to find the best match we will find the distance, the Lower the distance the better the match is.

Now on the basis of the index value we can display the name of the person and display it on the original Image.


**_6. Marking Attendance and details._**
In the last we will mark the attendance after finding the perfect match of the image including the current date and time.

![image](https://user-images.githubusercontent.com/74240933/113142419-7bf6bb00-9248-11eb-9e3d-09bcbcf19ce2.png)

The Attendance record will be maintained in an “Attendance.csv” file. It will contain name and current date and time.
