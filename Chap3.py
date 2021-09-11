import  cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)
print(img)

cv2.line(img , (0,0),(300,300),(0,255,0),5)

cv2.rectangle(img,(200,200),(250,250),(0,255,0),3)
cv2.circle(img,(250,250),30,(255,255,0),5)

cv2.putText(img,"OpenCV",(300,100),cv2.FONT_HERSHEY_SIMPLEX,1,(0,150,0),5)


cv2.imshow("Image",img)

cv2.waitKey(0)