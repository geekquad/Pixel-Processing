import cv2
import dlib

# Load the detector
detector = dlib.get_frontal_face_detector()

# Load the predictor
predictor = dlib.shape_predictor("./Models/shape_predictor_68_face_landmarks.dat")

# read the image
cap = cv2.VideoCapture(0)
i=0
while True:
    _, frame = cap.read()
    #choose any path u want to here, this will just be temporary
    path = 'C:\\imgs\\img'+str(i)+'.jpg'
    cv2.imwrite(path,frame)
    i = i+1
    # Converting image into grayscale
    gray = cv2.cvtColor(src=frame, code=cv2.COLOR_BGR2GRAY)

    # Use detector to find landmarks
    faces = detector(gray)

    for face in faces:
        x1 = face.left()  # left point
        y1 = face.top()  # top point
        x2 = face.right()  # right point
        y2 = face.bottom()  # bottom point

        # Create landmark object
        landmarks = predictor(image=gray, box=face)

        # Loop through all the points
        for n in range(0, 68):
            x = landmarks.part(n).x
            y = landmarks.part(n).y

            # Draw a circle for each landmark point we detect
            cv2.circle(img=frame, center=(x, y), radius=1, color=(0, 255, 0), thickness=-1)

    # show the image
    cv2.imshow(winname="Face", mat=frame)

    # Exit when escape key is pressed
    if cv2.waitKey(delay=1) == 27:
        break

# When everything done, release the video capture and video write objects
cap.release()

# Close all windows
cv2.destroyAllWindows()