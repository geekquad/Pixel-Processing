import cv2
import time
import matplotlib.pyplot as plt 
import numpy as np 
import os
import sys
import argparse

protoFile = "./pose_deploy_linevec.prototxt"
weightsFile = "pose/coco/pose_iter_440000.caffemodel"

if not os.path.exists(weightsFile):
	print('WeightsFile not Found. Please make sure you have run getModels.sh file before running this.')
	sys.exit()

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", help = "Input: Image or Video. WebCam: By Default",default=0,required=False)
parser.add_argument('-w','--width',help='Width of Image',default=300,required=False)
parser.add_argument('-l','--height',help='Height of Image',default=300,required=False)
parser.add_argument('-th','--threshold',help='Confidence Score',default=0.1,required=False)
parser.add_argument('-o','--Output',help='Output where to save the file',required=False,action='store_true')
args = parser.parse_args()


net = cv2.dnn.readNetFromCaffe(protoFile, weightsFile)
cap = cv2.VideoCapture(args.input)

while True:


	_ , frame = cap.read()

	frameCopy = np.copy(frame)

	frameWidth = frame.shape[1]
	frameHeight = frame.shape[0]

	threshold = args.threshold

	inWidth = int(args.width)
	inHeight = int(args.height)

	posePairs = [ [1,0],[1,2],[1,5],[2,3],[3,4],[5,6],[6,7],[1,8],[8,9],[9,10],[1,11],[11,12],[12,13],[0,14],[0,15],[14,16],[15,17]]

	inputBlob = cv2.dnn.blobFromImage(frame, 1.0 / 255, (inWidth, inHeight), (0, 0, 0), swapRB=False, crop=False)

	# Set the prepared object as the input blob of the network
	net.setInput(inputBlob)

	output = net.forward()

	H = output.shape[2]
	W = output.shape[3]
	points = []
	for i in range(18):
		
		probMap = output[0, i, :, :]
	 
		
		minVal, prob, minLoc, point = cv2.minMaxLoc(probMap)
		 
		
		x = (frameWidth * point[0]) / W
		y = (frameHeight * point[1]) / H
	 
		if prob > threshold : 
			cv2.circle(frame, (int(x), int(y)), 10, (0, 255, 255), thickness=-1, lineType=cv2.FILLED)
			#cv2.putText(frame, "{}".format(i), (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3, lineType=cv2.LINE_AA)
	 
			points.append((int(x), int(y)))
		else :
			points.append(None)

	for pair in posePairs:
		partA = pair[0]
		partB = pair[1]

		if points[partA] and points[partB]:
			cv2.line(frame, points[partA], points[partB], (0, 255, 255), 2)
			cv2.circle(frame, points[partA], 5, (0, 0, 255), thickness=-1, lineType=cv2.FILLED)

 
	cv2.imshow("Output-Keypoints",frame)
	
	if cv2.waitKey(1)==27:
		break

cap.release()
cv2.destroyAllWindows()
