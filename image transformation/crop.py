import cv2

image = cv2.imread("D:\open CV\pic\lw.jpg")

if image is not None:
  print("image loaded successfully")
  resized = image[0:800, 0:809]

  cv2.imshow("original image", image)
  cv2.imshow("resized image", resized)

  cv2.waitKey(0)
  cv2.destroyAllWindows()

else :
  print("image is not loaded successfully")