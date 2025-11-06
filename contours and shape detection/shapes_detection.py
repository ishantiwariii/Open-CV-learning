# first here is some conceptual notes

"""
cv2.approxPolyDP(curve, epsilon, closed)

This function approximates a contour shape to another shape with fewer vertices — depending on the precision you specify.
It is widely used to detect shapes like triangle, rectangle, circle, etc.cv2.approxPolyDP(curve, epsilon, closed)
This function approximates a contour shape to another shape with fewer vertices — depending on the precision you specify.
It is widely used to detect shapes like triangle, rectangle, circle, etc.


| Parameter | Description                                                                                     |
| --------- | ----------------------------------------------------------------------------------------------- |
| `curve`   | The contour you want to approximate (one contour from `findContours()`)                         |
| `epsilon` | The **maximum distance** between the original contour and its approximation — controls accuracy |
| `closed`  | Boolean — `True` if the shape is closed (e.g., circle, polygon), `False` if open                |

cv2.arcLength() → Calculates the perimeter of a contour (used to scale epsilon).
epsilon (0.01 * or 0.02 * perimeter) → The smaller the epsilon, the closer the approximation is to the original shape.

"""


"""basically here is the workflow 

Find contours
↓
for each contour:
    compute perimeter
    approximate contour
    draw contour
    count vertices
    get bounding rectangle
    determine shape type
    put shape name
show result
"""


import cv2

image = cv2.imread(r"D:\open CV\pic\image.png")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

_ , frame = cv2.threshold(gray, 100, 250  ,cv2.THRESH_BINARY)

contours , hierarchy = cv2.findContours(frame,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for contour in contours:
  area = cv2.contourArea(contour)
  if area < 1000:   # ignore small detections
        continue
  perimeter = cv2.arcLength(contour, True)

  approx = cv2.approxPolyDP(contour, 0.01 * perimeter, True)


  vertices = len(approx)

  if vertices == 3 :
    shapename = "triangle"

  elif vertices == 4 :
    shapename = "rectangle"

  elif vertices == 5 :
    shapename = "pentagon"

  elif vertices > 5:  
    shapename = "circle"
  else :
    shapename = "shape not found"

  cv2.drawContours(image, [approx], 0, (0, 255, 0), 3)
  x = approx.ravel()[0]
  y = approx.ravel()[-1] - 10
  cv2.putText(image, shapename, (x,y), cv2.FONT_HERSHEY_COMPLEX, 1.2, (0, 0 , 255),5 )

cv2.imshow("shape detection", image)
cv2.waitKey()
cv2.destroyAllWindows()