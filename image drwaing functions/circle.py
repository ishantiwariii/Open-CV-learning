import cv2

image = cv2.imread(r"D:\open CV\pic\LH.jpg")
pt1= (310, 400)
color= (225, 0 , 0)
thickness= 4

# if in thickness i pass -1 then it will fill the circle 

if image is not None:
  print("the image is successfully loaded")
  cv2.imshow("original image", image)
  
  # here is the syntax for circle on image
  cv2.circle(image, pt1, 300, color, thickness)
  cv2.imshow("line on image" , image)

  cv2.waitKey(0)
  cv2.destroyAllWindows()
else:
  print("the image is not loaded")