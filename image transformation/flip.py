import cv2

image = cv2.imread("D:\open CV\pic\LH.jpg")

if image is None :
  print("the image is not loaded")

else:
  flipped_ver = cv2.flip(image, 0)
  flipped_hor = cv2.flip(image, 1)
  flipped_both = cv2.flip(image, -1)

  cv2.imshow("original", image)
  cv2.imshow("flipped ver", flipped_ver)
  cv2.imshow("flipped hor", flipped_hor)
  cv2.imshow("flipped ver_hor", flipped_both)

  cv2.waitKey(0)
  cv2.destroyAllWindows()