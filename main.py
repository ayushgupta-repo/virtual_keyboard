# This file contains only one module of project that is virtual keyboard section.

# This module of the project basically provides the functionality of using keyboard to type in something like notepad based on detection of hand tracking and detection.

# We used OpenCV library for this project.

# importing packages and libraries
import cv2
from HandTrackingModule import handDetector

# using webcam as it's id is 0 to create video capturing device
cap = cv2.VideoCapture(0)

# resizing video capturing dimensions
cap.set(3, 1280)  # width
cap.set(4, 720)  # height

# creating handdetector object

# providing higher confidence value as by mistake key does not get pressed
detector = handDetector(detectionCon=0.8)


class Button():
    def __init__(self, pos, text, size=[85, 85]):
        self.pos = pos
        self.size = size
        self.text = text
        x, y = self.pos
        w, h = self.size
        # Creating rectangular boxes that contains font
        cv2.rectangle(img, self.pos, (x+w, y+h), (255, 0, 255), cv2.FILLED)

        # putting text on the image
        cv2.putText(img, self.text, (x + 20, y + 65), cv2.FONT_HERSHEY_PLAIN,
                    4, (255, 255, 255), 4)


# Creating button list
buttonList = []

while True:
    success, img = cap.read()

    # finding hands from the image/webcam
    img = detector.findHands(img)

    lmList = detector.findPosition(img, False)

    # Creating buttons object with loop
    for x in range(0, 5):
        buttonList.append(Button([100*x+50, 100], "Q"))

    # img = myButton.draw(img)
    # img = myButton1.draw(img)
    # img = myButton2.draw(img)

    cv2.imshow('Image', img)
    cv2.waitKey(1)

    # q button pressing to exit the prompt
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
