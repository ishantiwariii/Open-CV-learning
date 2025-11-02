import cv2

image = cv2.imread(r"D:\open CV\pic\LH.jpg")

if image is not None:
  h , w , c  = image.shape
  print(f"height is {h} , weight is {w} , color channel is {c}")

else :
  print("can't find the image")