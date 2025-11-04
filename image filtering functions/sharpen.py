import cv2
import numpy as np

import cv2

image = cv2.imread(r"D:\open CV\pic\06891d8b88f46ecd16ef32dc52664722.jpg")

kernal = np.array([
  [0 , -1 , 0],
  [-1, 5, -1],
  [0, -1, 0]]
)

if image is not None:
  print("image is loaded")

  sharpen = cv2.filter2D(image, -1, kernal)
  cv2.imshow("original", image)
  cv2.imshow("blurred", sharpen)

  cv2.waitKey(0)
  cv2.destroyAllWindows()

else:
  print("Image not loaded")  
