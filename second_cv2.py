import cv2
import sys
img=cv2.imread('./cat.jpg')

if img is None:
    sys.exit('Could not fiund')

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
resized_img = cv2.resize(gray_img,dsize=(0,0),fx=0.5,fy=0.5)
cv2.imshow("original",img)
cv2.imshow("grey",gray_img)
cv2.imshow("resized",resized_img)
cv2.waitKey()
cv2.destroyWindow()
