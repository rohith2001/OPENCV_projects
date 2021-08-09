import cv2
import numpy as np
img =cv2.imread("pic.jpg")
#edges
gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img=cv2.resize(img,(480,640))
gray=cv2.resize(gray,(480,640))
gray = cv2.medianBlur(gray,5)
#print(img.shape)
# this edge background will be coverted to black when we apply the canny method
#edges  = cv2.Canny(gray,50,200)
# this background will be white in adaptive threshold
edges = cv2.adaptiveThreshold(gray,5,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,3,11)
# cartoonisation
color=cv2.bilateralFilter(img,5,200,200)
color=cv2.resize(color,(480,640))
cartoon = cv2.bitwise_and(color,color,mask=edges)
cv2.imshow("image",img)
#cv2.imshow("edges",edges)
cv2.imshow("cartoon",cartoon)
cv2.waitKey(0)
cv2.destroyAllWindows()
