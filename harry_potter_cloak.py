import cv2
import numpy as np
import time
#print(cv2.__version__)
capture_video=cv2.VideoCapture(0)
time.sleep(3)
background=0

for i in range(60):
    ret,background=capture_video.read()
    background=np.flip(background,axis=1)

while(capture_video.isOpened()):
    ret,image=capture_video.read()
    if not ret:
        break
    image=np.flip(image,axis=1)
    hsv=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
    lower_red=np.array([100,40,40])
    upper_red=np.array([100,255,255])
    mask1=cv2.inRange(hsv,lower_red,upper_red)
    lower_red=np.array([155,40,40])
    upper_red=np.array([180,255,255])
    mask2=cv2.inRange(hsv,lower_red,upper_red)
    mask=mask1+mask2
    mask=cv2.morphologyEx(mask,cv2.MORPH_OPEN,np.ones((5,5),np.uint8),iterations=2)
    mask=cv2.dilate(mask,np.ones((5,5),np.uint8),iterations=2)
    mask3=cv2.bitwise_not(mask)

    res1=cv2.bitwise_and(background,background,mask=mask)
    res2=cv2.bitwise_and(image,image,mask=mask3)
    final_output=cv2.addWeighted(res1,1,res2,1,0)
    #cv2.imshow("mask3",mask3)
    cv2.imshow("final_output",final_output)
    k=cv2.waitKey(10)
    if k==27:
        break
capture_video.release()
cv2.destroyAllWindows()