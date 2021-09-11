import cv2
import numpy as np

img = cv2.imread("/Users/anubhav/Desktop/lena.png")

imgHor = np.hstack((img,img))

imgVir =  np.vstack((img,img))

cv2.imshow("Image",imgHor)
cv2.imshow("Image Vir",imgVir)


cv2.waitKey(0)

