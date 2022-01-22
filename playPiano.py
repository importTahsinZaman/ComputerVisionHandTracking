import cvzone
import cv2
from pynput.keyboard import Key, Controller
import time

keyboard = Controller()
cap = cv2.VideoCapture(0)
detector = cvzone.HandDetector(maxHands=1, detectionCon=0.7)

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img)
    if lmList:
        fingers = detector.fingersUp()
        print(fingers)
    cv2.imshow("Image", img)
    cv2.waitKey(1)

    if fingers[0] == 0:
        keyboard.press('1')
        keyboard.release('1')

    if fingers[1] == 0:
        keyboard.press('2')
        keyboard.release('2')

    if fingers[2] == 0:
        keyboard.press('3')
        keyboard.release('3')

    if fingers[3] == 0:
        keyboard.press('4')
        keyboard.release('4')

    if fingers[4] == 0:
        keyboard.press('5')
        keyboard.release('5')


