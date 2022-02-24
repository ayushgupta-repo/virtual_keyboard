# This file contains only one module of project that is virtual keyboard section.

# This module of the project basically provides the functionality of using keyboard to type in something like notepad based on detection of hand tracking and detection.

# We used OpenCV library for this project.

# importing packages and libraries
import cv2

# using webcam as it's id is 0 to create video capturing device
cap = cv2.VideoCapture(0)

# resizing video capturing dimensions
cap.set(3, 1280)
cap.set(4, 720)

while True:
    success, img = cap.read()
    cv2.imshow('Image', img)
    cv2.waitKey(1)
