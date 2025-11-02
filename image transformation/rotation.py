import cv2

image = cv2.imread("D:\open CV\pic\lw.jpg")

if image is None:
  print("image not found")

else:
  print("image is loaded successfully! ")
  h, w, c = image.shape
  center = (w//2 , h//2)
  m = cv2.getRotationMatrix2D(center, 90, 1.5)
  rotated = cv2.warpAffine(image, m, (w,h) )

  cv2.imshow("original image", image)
  cv2.imshow("rotated image", rotated)
  cv2.waitKey(0)
  cv2.destroyAllWindows()