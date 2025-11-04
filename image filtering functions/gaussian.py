# 🧠 What is Blurring?

# Blurring means replacing each pixel’s value with some form of average of its neighboring pixels.
# Different blur methods define “average” differently — that’s what gives us different types of blur.

#  types of blur 
# cv2.blur() → simple averaging
# cv2.GaussianBlur() → smoother, natural blur
# cv2.medianBlur() → best for salt-and-pepper noise

# Gaussian blur 
# Uses a Gaussian distribution (bell curve) to give more weight to the center pixels and less to distant ones.
# This creates a natural, smooth blur.

import cv2 

image = cv2.imread(r"D:\open CV\pic\06891d8b88f46ecd16ef32dc52664722.jpg")

if image is not None:
  print("image is loaded")

  blurred = cv2.GaussianBlur(image, (13,13), 0)
  cv2.imshow("original", image)
  cv2.imshow("blurred", blurred)

  cv2.waitKey(0)
  cv2.destroyAllWindows()

else:
  print("Image not loaded")  
