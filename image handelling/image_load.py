import cv2

image = cv2.imread(r"D:\open CV\pic\LH.jpg")

if image is not None :
  print("image loaded successfully")

else:
  print("image is not loaded successfully")