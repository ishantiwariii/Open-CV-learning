import cv2

image = cv2.imread(r"D:\open CV\pic\06891d8b88f46ecd16ef32dc52664722.jpg")

if image is not None:
  print("image is loaded")

  blurred = cv2.medianBlur(image, 5)
  cv2.imshow("original", image)
  cv2.imshow("blurred", blurred)

  cv2.waitKey(0)
  cv2.destroyAllWindows()

else:
  print("Image not loaded")  
