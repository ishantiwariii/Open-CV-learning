import cv2

image = cv2.imread(r"D:\open CV\pic\LH.jpg")
pt1= (310, 400)
color= (225, 156 , 0)
thickness= 4

if image is not None:
  print("the image is successfully loaded")
  cv2.imshow("original image", image)
  
# here is the syntax for putting text on image 
  cv2.putText(image, "Lewis Hamilton", (150, 750), cv2.FONT_HERSHEY_SIMPLEX, 1.2, color, thickness)
  cv2.imshow("line on image" , image)

  cv2.waitKey(0)
  cv2.destroyAllWindows()
else:
  print("the image is not loaded")