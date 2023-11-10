import cv2
from subprocess import call
import numpy as np
import subprocess
import time
import os
import glob
import inspect
import webbrowser

CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
	"bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
	"dog", "horse", "motorbike", "person", "pottedplant", "sheep",
	"sofa", "train", "tvmonitor"]
COLORS = np.random.uniform(0, 255, size=(len(CLASSES), 3))
print("[INFO] loading model...")
net = cv2.dnn.readNetFromCaffe("MobileNetSSD_deploy.prototxt.txt", "MobileNetSSD_deploy.caffemodel")
image = cv2.imread("images/4.jpg")
(h, w) = image.shape[:2]
blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 0.007843, (300, 300), 127.5)
print ()
print("[INFO] computing object detections...")
net.setInput(blob)
detections = net.forward()
for i in np.arange(0, detections.shape[2]):
	confidence = detections[0, 0, i, 2]
	if confidence > 0.2:
		idx = int(detections[0, 0, i, 1])
		box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
		(startX, startY, endX, endY) = box.astype("int")
		label = "{}: {:.2f}%".format(CLASSES[idx], confidence * 100)
		print("[INFO] {}".format(label))
	
		cv2.rectangle(image, (startX, startY), (endX, endY),
			COLORS[idx], 2)
		y = startY - 15 if startY - 15 > 15 else startY + 15
		cv2.putText(image, label, (startX, y),
			cv2.FONT_HERSHEY_SIMPLEX, 0.5, COLORS[idx], 2)
		
		
		
cv2.imshow("Output", image)
cv2.waitKey(0)
new=2
d=CLASSES[idx]
if(d=='bottle'):
        url='https://en.wikipedia.org/wiki/Bottle'
        webbrowser.open(url,new=new)
if(d=='chair'):
        url='https://en.wikipedia.org/wiki/Chair'
        webbrowser.open(url,new=new)
if(d=='person'):
        url='https://en.wikipedia.org/wiki/Person'
        webbrowser.open(url,new=new)
if(d=='cat'):
        url='https://en.wikipedia.org/wiki/Cat'
        webbrowser.open(url,new=new)
if(d=='dog'):
        url='http://www.vetstreet.com/dogs/'
        webbrowser.open(url,new=new)        
else:
        print ('bye')

                        


