import cv2
import numpy as np


frame_width = 640
frame_height = 480
cap = cv2.VideoCapture(1)
cap.set(3, frame_width)
cap.set(4, frame_height)
cap.set(10, 130)

while True:
    success, img =cap.read()
    cv2.imshow("Result",img)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
cap.release()
cap.destroyAllWindows()
