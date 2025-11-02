import cv2

image = cv2.imread(r"D:\open CV\pic\LH.jpg")

if image is not None :
  success = cv2.imwrite("lewis_hamilton.jpg" , image)
  if success:
    print("image is successfully saved")
  else:
    print("image is not saved successfully")
else:
  print("image is not found")

