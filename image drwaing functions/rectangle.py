import cv2

image = cv2.imread(r"D:\open CV\pic\LH.jpg")
pt1= (30, 50)
pt2 = (500, 700)
color= (225, 0 , 0)
thickness= 4

if image is not None:
  print("the image is successfully loaded")
  cv2.imshow("original image", image)
  
  # here is the syntax for rectangle on image
  cv2.rectangle(image,pt1,pt2, color, thickness)
  cv2.imshow("line on image" , image)

  cv2.waitKey(0)
  cv2.destroyAllWindows()
else:
  print("the image is not loaded")