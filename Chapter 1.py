import cv2
import numpy as np

kernel= np.ones((5,5),np.uint8)

img = cv2.imread("/Users/anubhav/Desktop/lena.png")
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)

imgCanny= cv2.Canny(imgGray,150,150)

imgDia = cv2.dilate(imgCanny,kernel,iterations=1)

imgEroded = cv2.erode(imgCanny,kernel,iterations=1)

cv2.imshow("Output image" , imgEroded)



cv2.waitKey(0)


