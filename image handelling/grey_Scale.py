import cv2 

image = cv2.imread(r"D:\open CV\pic\f1.jpg")

if image is not None :
  grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  cv2.imshow("the grey f1", grey)
  cv2.waitKey(0)
  cv2.destroyAllWindows()

else:
  print("image not found")