import cv2

image = cv2.imread(r"D:\open CV\pic\LH.jpg")

if image is not None :
  cv2.imshow("lewis hamilton", image)
  cv2.waitKey(0)
  cv2.destroyAllWindows()

else:
  print("image is not loaded successfully")