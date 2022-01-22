import cvzone
import cv2

cap = cv2.VideoCapture(0)
detector = cvzone.HandDetector(maxHands=1, detectionCon=0.7)
mySerial = cvzone.SerialObject("COM4", 9600, 1)

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img)
    if lmList:
        fingers = detector.fingersUp()
        print(fingers)
        mySerial.sendData(fingers)
    cv2.imshow("Image", img)
    cv2.waitKey(1)

