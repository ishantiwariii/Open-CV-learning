import cv2

image = cv2.imread(r"D:\open CV\pic\kgp1 (1).jpg", cv2.IMREAD_GRAYSCALE)

edged = cv2.Canny(image, 120, 255)

cv2.imshow("original image", image)
cv2.imshow("canny edge", edged)

cv2.waitKey(0)
cv2.destroyAllWindows()