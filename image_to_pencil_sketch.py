import cv2
image=cv2.imread("pic.jpg")
gray_image= cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
gray_image=cv2.resize(gray_image,(480,640))
gray_color_inv=255-gray_image
gray_color_inv=cv2.GaussianBlur(gray_color_inv,(21,21),0)
output=cv2.divide(gray_image,255-gray_color_inv,scale=256.0)
gray_image=cv2.Canny(gray_image,89,158,edges=7)

#cv2.imshow("image",gray_image)
#cv2.imshow("inverted",gray_color_inv)
cv2.imshow("pencil",output)
#cv2.imwrite('pic_converted.jpg',output)
print("saved")
cv2.waitKey(0)
cv2.destroyAllWindows()