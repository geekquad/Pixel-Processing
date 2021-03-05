import cv2
import dlib

# Load the detector
detector = dlib.get_frontal_face_detector()

# Load the predictor
predictor = dlib.shape_predictor(".//Models//shape_predictor_68_face_landmarks.dat")

# read the image
# Loading the image and converting it to grayscale
image= cv2.imread('.//Assets//sample.png')
gray= cv2.imread('.//Assets//sample.png', cv2.IMREAD_GRAYSCALE)

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
		cv2.circle(img=image, center=(x, y), radius=1, color=(0, 255, 0), thickness=-1)

while(True):
	# show the image
	cv2.imshow(winname="Press 'esc' key to exit", mat=image)

	# Exit when escape key is pressed
	if cv2.waitKey(delay=1) == 27:
		break

# Close all windows
cv2.destroyAllWindows()