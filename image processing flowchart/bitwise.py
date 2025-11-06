import cv2
import numpy as np 

img1= np.zeros((300,300), dtype="uint8")
img2= np.zeros((300,300), dtype="uint8")

cv2.circle(img1, (150,150), 100, 255, -1)
cv2.rectangle(img2, (100,100), (250, 250), 255, -1)

bit_or = cv2.bitwise_or(img1,img2)
bit_not = cv2.bitwise_not(img1)
bit_and = cv2.bitwise_and(img1, img2)

cv2.imshow("circle", img1)
cv2.imshow("rectagnle", img2)
cv2.imshow("and", bit_and)
cv2.imshow("or", bit_or)
cv2.imshow("not", bit_not)


cv2.waitKey(0)
cv2.destroyAllWindows()