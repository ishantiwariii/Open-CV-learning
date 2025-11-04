import cv2

image = cv2.imread(r"D:\open CV\pic\kgp1 (1).jpg", cv2.IMREAD_GRAYSCALE)

ret, frame = cv2.threshold(image, 100, 255, cv2.THRESH_BINARY)

cv2.imshow("original image", image)
cv2.imshow("canny edge", frame)

cv2.waitKey(0)
cv2.destroyAllWindows()