import numpy as np
import argparse
import cv2
from gtts import gTTS
import os
import pygame
from pygame import mixer


CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
	"bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
	"dog", "horse", "motorbike", "person", "pottedplant", "sheep",
	"sofa", "train", "tvmonitor"]
COLORS = np.random.uniform(0, 255, size=(len(CLASSES), 3))
print("[INFO] loading model...")
net = cv2.dnn.readNetFromCaffe("MobileNetSSD_deploy.prototxt.txt", "MobileNetSSD_deploy.caffemodel")
image = cv2.imread("images/example_06.jpg")
(h, w) = image.shape[:2]
blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 0.007843, (300, 300), 127.5)
print ()
print("[INFO] computing object detections...")
net.setInput(blob)
detections = net.forward()
labels=''
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
		labels=labels+str(' ')+label
tts = gTTS(text=labels, lang='en')
tts.save("good.mp3")
os.system("mpg321 good.mp3")
mixer.init()
mixer.music.load('good.mp3')
mixer.music.play()
		
		
cv2.imshow("Output", image)
cv2.waitKey(0)



