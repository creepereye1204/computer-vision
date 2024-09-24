import cv2
import sys
import numpy as np

img = cv2.imread('./cat.jpg')

if img is None:
    sys.exit('Could not find the image.')


I = 0.299 * img[:, :, 2] + 0.587 * img[:, :, 1] + 0.114 * img[:, :, 0]  


I = I.astype(np.uint8)


cv2.imshow("Grayscale Image", I)

cv2.waitKey(0)
cv2.destroyAllWindows()
