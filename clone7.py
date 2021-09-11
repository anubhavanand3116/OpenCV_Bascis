import cv2
import numpy as np


def  empty(a):
    pass

path = "/Users/anubhav/Desktop/car.png"

cv2.namedWindow("TrackBars")

cv2.resizeWindow("TrackBars",640,340)


img= cv2.imread(path)
cv2.createTrackbar("Hue Min","TrackBars",0,179,empty)
cv2.createTrackbar("Hue Max","TrackBars",17,179,empty)

cv2.createTrackbar("Sat Min","TrackBars",88,255,empty)
cv2.createTrackbar("Sat Max","TrackBars",25,255,empty)

cv2.createTrackbar("Val Min","TrackBars",45,255,empty)
cv2.createTrackbar("Val MAx","TrackBars",65,255,empty)


lower= np.array([h_min,s_min,v_min])
upper= np.array([h_max,s_max,v_max])

mask= cv2.inRange(imgHSV,lower,upper)


cv2.imshow("Original",img)
cv2.imshow("HSV",imgHSV)
cv2.imshow("Mask",mask)

cv2.waitKey(0)
