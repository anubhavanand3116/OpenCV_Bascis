import cv2
import numpy as np

img = cv2.imread("/Users/anubhav/Desktop/cards.jpeg")

cv2.imshow("Image", img) 

width ,height =25,35

pts1 = np.float32([[111,219],[289,188],[154,482],[352,40]])

pts2 =np.float32([[0,0],[width,0],[0,height],[width,height]])


matrix = cv2.perspectiveTransform(pts1,pts2)

imgOut = cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow("Image",img)
cv2.imshow("output",imgOut)


cv2.waitKey(0)