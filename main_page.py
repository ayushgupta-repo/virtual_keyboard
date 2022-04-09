# Creating mainmenu screen

import cv2
from HandTrackingModule import handDetector
from time import sleep

cap = cv2.VideoCapture(0)

cap.set(3, 1280)
cap.set(4, 720)

detector = handDetector(detectionCon=0.8)

# creating option menu
keys = ['AI VIRTUAL KEYBOARD', 'AI VIRTUAL MOUSE', 'AI VOLUME CONTROLLER']

while True:
    success, img = cap.read()

    img = detector.findHands(img)

    lmList = detector.findPosition(img, False)

    size = [0, 200, 400]

    # creating shapes to make menu page

    cv2.rectangle(img, (50, 40), (1150, 130),
                  (175, 0, 175), cv2.FILLED)

    cv2.rectangle(img, (50, 240), (1150, 330),
                  (175, 0, 175), cv2.FILLED)

    cv2.rectangle(img, (50, 440), (1150, 530),
                  (175, 0, 175), cv2.FILLED)

    # providing text from menu
    for i in range(len(keys)):
        cv2.putText(img, keys[i], (60, 100+size[i]), cv2.FONT_HERSHEY_PLAIN,
                    5, (255, 255, 255), 5)

    # getting distance and performing choice operation
    if lmList:
        l, _, _ = detector.findDistance(lmList[8][1:3], lmList[12][1:3], img)

        if l < 60:

            # below code is for option 1 selection
            if (50 <= lmList[7][1] <= 1150) and (60 <= lmList[7][2] <= 150):
                cv2.rectangle(img, (50, 40), (1150, 130),
                              (0, 255, 0), cv2.FILLED)
                cv2.putText(img, keys[0], (60, 100+size[0]), cv2.FONT_HERSHEY_PLAIN,
                            5, (255, 255, 255), 5)

                string = 'AI Virtual Keyboard'

                if string:

                    # put function calling part over here
                    print(string)

            # below code is for option 2 selection
            if (50 <= lmList[7][1] <= 1150) and (260 <= lmList[7][2] <= 350):
                cv2.rectangle(img, (50, 240), (1150, 330),
                              (0, 255, 0), cv2.FILLED)
                cv2.putText(img, keys[1], (60, 100+size[1]), cv2.FONT_HERSHEY_PLAIN,
                            5, (255, 255, 255), 5)

                string = 'AI Virtual Mouse'

                if string:

                    # put function calling part over here
                    print(string)

            # below code is for option 3 selection
            if (50 <= lmList[7][1] <= 1150) and (460 <= lmList[7][2] <= 550):
                cv2.rectangle(img, (50, 440), (1150, 530),
                              (0, 255, 0), cv2.FILLED)
                cv2.putText(img, keys[2], (60, 100+size[2]), cv2.FONT_HERSHEY_PLAIN,
                            5, (255, 255, 255), 5)

                string = 'AI Volume Controller'

                if string:

                    # put function calling part over here
                    print(string)

            sleep(0.25)

    cv2.imshow('Image', img)
    cv2.waitKey(1)

    # q button pressing to exit the prompt
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
