import numpy as np  
import cv2  
import dlib  
from scipy.spatial import distance as dist  
from scipy.spatial import ConvexHull
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--funnyeye', help="Funny Eye Filter", default=False)
parser.add_argument('--moustache', help="Mustache Filter", default=False)
parser.add_argument('--santaclaus', help="Santa Claus Hat and Cap Filter", default=False)
args = parser.parse_args()  

def eye_size(eye):
    eyeWidth = dist.euclidean(eye[0], eye[3])
    hull = ConvexHull(eye)
    eyeCenter = np.mean(eye[hull.vertices, :], axis=0)
    eyeCenter = eyeCenter.astype(int)

    return int(eyeWidth), eyeCenter


def place_eye(frame, eyeCenter, eyeSize, filter_img, mask, mask_inv):  
	eyeSize = int(eyeSize * 1.5)  

	x1 = int(eyeCenter[0,0] - (eyeSize/2))  
	x2 = int(eyeCenter[0,0] + (eyeSize/2))  
	y1 = int(eyeCenter[0,1] - (eyeSize/2))  
	y2 = int(eyeCenter[0,1] + (eyeSize/2))  

	h, w = frame.shape[:2]  

	# check for clipping  
	if x1 < 0:  
	 x1 = 0  
	if y1 < 0:  
	 y1 = 0  
	if x2 > w:  
	 x2 = w  
	if y2 > h:  
	 y2 = h  

	# re-calculate the size to avoid clipping  
	eyeOverlayWidth = x2 - x1  
	eyeOverlayHeight = y2 - y1  

	# calculate the masks for the overlay  
	eyeOverlay = cv2.resize(filter_img, (eyeOverlayWidth,eyeOverlayHeight), interpolation = cv2.INTER_AREA)  
	mask = cv2.resize(mask, (eyeOverlayWidth,eyeOverlayHeight), interpolation = cv2.INTER_AREA)  
	mask_inv = cv2.resize(mask_inv, (eyeOverlayWidth,eyeOverlayHeight), interpolation = cv2.INTER_AREA)  

	# take ROI for the verlay from background, equal to size of the overlay image  
	roi = frame[y1:y2, x1:x2]  

	# roi_bg contains the original image only where the overlay is not, in the region that is the size of the overlay.  
	roi_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)  

	# roi_fg contains the image pixels of the overlay only where the overlay should be  
	roi_fg = cv2.bitwise_and(eyeOverlay,eyeOverlay,mask = mask)  

	# join the roi_bg and roi_fg  
	dst = cv2.add(roi_bg,roi_fg)  

	# place the joined image, saved to dst back over the original image  
	frame[y1:y2, x1:x2] = dst


def funny_eyes(landmark, LEFT_EYE_POINTS, RIGHT_EYE_POINTS, frame, filter_img, mask, mask_inv):
    left_eye = landmark[LEFT_EYE_POINTS]
    right_eye = landmark[RIGHT_EYE_POINTS]
    lefteyesize, lefteyecenter = eye_size(left_eye)
    righteyesize, righteyecenter = eye_size(right_eye)
    place_eye(frame, lefteyecenter, lefteyesize, filter_img, mask, mask_inv)  
    place_eye(frame, righteyecenter, righteyesize, filter_img, mask, mask_inv)


def nose_dimensions(nose):
    height = dist.euclidean(nose[0], nose[3])
    width = dist.euclidean(nose[4], nose[8])
    return int(height), int(width)


def place_moustache(frame, nose, nose_w, nose_h, filter_img, mask, mask_inv):
    orig_height, orig_width = filter_img.shape[:2]
    mustacheWidth = int(3 * nose_w)
    mustacheHeight = int(mustacheWidth * orig_height / orig_width)

    x1 = int(nose[8, 0] - nose_w - (mustacheWidth/4))
    x2 = int(nose[8, 0] + (mustacheWidth/4))
    y1 = int(nose[8, 1] - (mustacheHeight/2))
    y2 = int(nose[8, 1] + (mustacheHeight/2))

    h, w = frame.shape[:2]

    if x1 < 0:
        x1 = 0
    if y1 < 0:
        y1 = 0
    if x2 > w:
        x2 = w
    if y2 > h:
        y2 = h

    mustacheWidth = int(x2 - x1)
    mustacheHeight = int(y2 - y1)

    # Re-size the original image and the masks to the mustache sizes
    # calcualted above
    mustache = cv2.resize(filter_img, (mustacheWidth,mustacheHeight), interpolation = cv2.INTER_AREA)
    mask = cv2.resize(mask, (mustacheWidth,mustacheHeight), interpolation = cv2.INTER_AREA)
    mask_inv = cv2.resize(mask_inv, (mustacheWidth,mustacheHeight), interpolation = cv2.INTER_AREA)

    # take ROI for mustache from background equal to size of mustache image
    roi = frame[y1:y2, x1:x2]

    # roi_bg contains the original image only where the mustache is not
    # in the region that is the size of the mustache.
    roi_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)

    # roi_fg contains the image of the mustache only where the mustache is
    roi_fg = cv2.bitwise_and(mustache,mustache,mask = mask)

    # join the roi_bg and roi_fg
    dst = cv2.add(roi_bg,roi_fg)

    # place the joined image, saved to dst back over the original image
    frame[y1:y2, x1:x2] = dst

def santa_moustache(frame, nose, nose_w, nose_h, filter_img, mask, mask_inv):
    orig_height, orig_width = filter_img.shape[:2]
    mustacheWidth = int(5 * nose_w)
    mustacheHeight = int(mustacheWidth * orig_height / orig_width)

    x1 = int(nose[8, 0] - nose_w - (mustacheWidth/4))
    x2 = int(nose[8, 0] + (mustacheWidth/4))
    y1 = int(nose[8, 1])
    y2 = int(nose[8, 1] + (mustacheHeight/2))

    h, w = frame.shape[:2]

    if x1 < 0:
        x1 = 0
    if y1 < 0:
        y1 = 0
    if x2 > w:
        x2 = w
    if y2 > h:
        y2 = h

    mustacheWidth = int(x2 - x1)
    mustacheHeight = int(y2 - y1)

    # Re-size the original image and the masks to the mustache sizes
    # calcualted above
    mustache = cv2.resize(filter_img, (mustacheWidth,mustacheHeight), interpolation = cv2.INTER_AREA)
    mask = cv2.resize(mask, (mustacheWidth,mustacheHeight), interpolation = cv2.INTER_AREA)
    mask_inv = cv2.resize(mask_inv, (mustacheWidth,mustacheHeight), interpolation = cv2.INTER_AREA)

    # take ROI for mustache from background equal to size of mustache image
    roi = frame[y1:y2, x1:x2]

    # roi_bg contains the original image only where the mustache is not
    # in the region that is the size of the mustache.
    roi_bg = cv2.bitwise_and(roi, roi, mask = mask_inv)

    # roi_fg contains the image of the mustache only where the mustache is
    roi_fg = cv2.bitwise_and(mustache, mustache, mask = mask)

    # join the roi_bg and roi_fg
    dst = cv2.add(roi_bg,roi_fg)

    # place the joined image, saved to dst back over the original image
    frame[y1:y2, x1:x2] = dst

def santa_hat(frame, face, face_w, face_h, filter_img, mask, mask_inv):
	original_hat_h, original_hat_w = filter_img.shape[:2]
	hat_width = int(1.2 * face_w)
	hat_height = int(hat_width * original_hat_h / original_hat_w)
	# print(hat_height)
	face_x2, face_y1 = face
	#setting location of coordinates of witch
	hat_x1 = face_x2 - int(face_w/2) - int(hat_width/2) - 2
	hat_x2 = hat_x1 + hat_width
	hat_y1 = face_y1
	hat_y2 = int(hat_y1 - (hat_height*0.9))

	h, w = frame.shape[:2]

	#Conditions to check if any out of frame
	if hat_x1 < 0:
	  hat_x1 = 0
	if hat_y2 < 0:
	  hat_y2 = 0
	if hat_x2 > w:
	  hat_x2 = w
	if hat_y1 > h:
	  hat_y1 = h


	hat_width = int(hat_x2 - hat_x1)
	hat_height = int(hat_y1 - hat_y2)

	#resizing witch hat image to fit on face
	witch = cv2.resize(filter_img, (hat_width,hat_height), interpolation = cv2.INTER_AREA)
	mask = cv2.resize(mask, (hat_width,hat_height), interpolation = cv2.INTER_AREA)
	mask_inv = cv2.resize(mask_inv, (hat_width,hat_height), interpolation = cv2.INTER_AREA)

	#take ROI for witch from background that is equal to size of witch image
	roi = frame[hat_y2:hat_y1, hat_x1:hat_x2]

	#original image in background (bg) where witch is not
	roi_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
	roi_fg = cv2.bitwise_and(witch, witch, mask=mask)
	dst = cv2.add(roi_bg,roi_fg)

	#put back in original image
	frame[hat_y2:hat_y1, hat_x1:hat_x2] = dst

def santaclaus(landmarks, NOSE_POINTS, face, frame, filter_img_1, filter_img_2, mask_1, mask_2, mask_inv_1, mask_inv_2):
	nose = landmarks[NOSE_POINTS]
	nose_h, nose_w = nose_dimensions(nose)

	x1, x2, y1, y2 = face
	face_h = int(y1 - y2)
	face_w = int(x2 - x1)
	FACE = [x2, y1]
	# frame = cv2.circle(frame, (x2,y1), radius=1, color=(0, 0, 255))
	# cv2.rectangle(frame, (nose[8, 0]-nose_w, nose[8, 1]-nose_h), (nose[8, 0], nose[8, 1]), (255, 0, 0), 2)

	santa_moustache(frame, nose, nose_w, nose_h, filter_img_1, mask_1, mask_inv_1)
	santa_hat(frame, FACE, face_w, face_h, filter_img_2, mask_2, mask_inv_2)



def mustache(landmark, NOSE_POINTS, frame, filter_img, mask, mask_inv):
    nose = landmark[NOSE_POINTS]
    nose_h, nose_w = nose_dimensions(nose)
    # cv2.rectangle(frame, (nose[8, 0]-nose_w, nose[8, 1]-nose_h), (nose[8, 0], nose[8, 1]), (255, 0, 0), 2)

    place_moustache(frame, nose, nose_w, nose_h, filter_img, mask, mask_inv)

def create_mask(filter_img):
	mask = filter_img[:, :, 3]
	mask_inv = cv2.bitwise_not(mask)
	filter_img = filter_img[:, :, 0:3]
	return mask, mask_inv, filter_img

def main():
    print('IMPORTANT!!!!!!')
    print('To close the frame, press "q" key on your keyboard!')
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor("model/shape_predictor_68_face_landmarks.dat")

    FULL_POINTS = list(range(0, 68))  
    FACE_POINTS = list(range(17, 68))  
       
    JAWLINE_POINTS = list(range(0, 17))  
    RIGHT_EYEBROW_POINTS = list(range(17, 22))  
    LEFT_EYEBROW_POINTS = list(range(22, 27))  
    NOSE_POINTS = list(range(27, 36))  
    RIGHT_EYE_POINTS = list(range(36, 42))  
    LEFT_EYE_POINTS = list(range(42, 48))  
    MOUTH_OUTLINE_POINTS = list(range(48, 61))  
    MOUTH_INNER_POINTS = list(range(61, 68))

    if args.funnyeye:
      filter_img = cv2.imread('filters/eye.png', -1)
      mask, mask_inv, filter_img = create_mask(filter_img)
    if args.moustache:
      filter_img = cv2.imread('filters/moustache.png', -1)
      mask, mask_inv, filter_img = create_mask(filter_img)
    if args.santaclaus:
      filter_img_1 = cv2.imread('filters/beard.png', -1)
      filter_img_2 = cv2.imread('filters/santa-cap.png', -1)
      mask_1, mask_inv_1, filter_img_1 = create_mask(filter_img_1)
      mask_2, mask_inv_2, filter_img_2 = create_mask(filter_img_2)

    # filter_height, filter_width = filter_img.shape[:2]
    cap = cv2.VideoCapture(0)

    while True:
        _, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = detector(gray)
        for face in faces:
            x1 = face.left()
            y1 = face.top()
            x2 = face.right()
            y2 = face.bottom()
            # cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 3)

            landmarks = predictor(gray, face)
            face_landmark = []
            for p in landmarks.parts():
                face_landmark.append([p.x, p.y])

            landmark = np.matrix(face_landmark)
            if args.funnyeye:
                funny_eyes(landmark, LEFT_EYE_POINTS, RIGHT_EYE_POINTS, frame, filter_img, mask, mask_inv)
            if args.moustache:
                mustache(landmark, NOSE_POINTS, frame, filter_img, mask, mask_inv)
            if args.santaclaus:
              santaclaus(landmark, NOSE_POINTS, [x1, x2, y1, y2], frame, filter_img_1, filter_img_2, mask_1, mask_2, mask_inv_1, mask_inv_2)  

        cv2.imshow("Frame", frame)

        key = cv2.waitKey(1)
        if key == ord('q'):
            break

if __name__ == '__main__':
    main()