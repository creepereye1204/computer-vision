import cv2
import sys
img=cv2.imread('./cat.jpg')

if img is None:
    sys.exit('Could not fiund')
cv2.imshow("s",img)
cv2.waitKey()
cv2.destroyWindow()