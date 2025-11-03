# make a project where user will input a location of a image and then you will provide the options that what a user wants 
# option 1 - make a circle 
# option 2 - make a rectangle
# option 3 - make a line
# also the coordinates will be entered by a user 

import cv2

class Drawing :
  def __init__(self, radius = None, center= None, pt1 = None, pt2= None, location = None, image=None):
    self.path = location
    self.radius = radius
    self.image= image
    self.center = center
    self.pt1 = pt1
    self.pt2 = pt2
    self.color = (255, 0, 0)
    self.thickness = 5

    print("hey wassup! ")
    self.location()
  
# taking image location and reading it
  def location (self):
    self.path = input("enter the path of the image! ")
    self.image = cv2.imread(self.path)

    if self.image is not None:
      print("Image loaded successfully")
      self.choose()
    else:
      print("Image not loaded, Try again!")
      self.location()
  
# function to choose options 
  def choose (self):
    print(""" choose the functions you want to perform 
              choose 1 for making line on image 
              choose 2 for making circle on image
              choose 3 for making rectangle on image """)
    
    option = int(input("enter the number  - "))

    if option == 1 :
      self.line()
    elif option == 2:
      self.circle()
    elif option == 3:
      self.rectangle()
    else :
      print("choose valid option")
      self.choose()
  
# function to draw line 
  def line(self):
    print("enter the following value for line coordinates")
    x1, y1 = int (input("enter x1 - ")), int (input("enter y1 - "))
    x2, y2 = int (input("enter x2 - ")), int (input("enter y2 - "))
    self.pt1 = (x1, y1)
    self.pt2 = (x2, y2)
    
    cv2.line(self.image, self.pt1, self.pt2, self.color, self.thickness)
    cv2.imshow("with line image", self.image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    print("for save the image write yes or no")
    option = input("enter here - ")

    if option.lower() == "yes":
      self.save()
    else :
      self.choose()

# function to draw circle 
  def circle(self):
    x1, y1 = int (input("enter the center coordinate X1 - ")) ,int (input("enter the center coordinate Y1 - "))
    radius = int(input("Enter the radius (Pixel) - "))
    self.center = (x1, y1)
    self.radius = radius

    cv2.circle(self.image, self.center, self.radius,self.color, self.thickness)
    cv2.imshow("circled image", self.image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    print("for save the image write yes or no")
    option = input("enter here - ")

    if option.lower() == "yes":
      self.save()
    else :
      self.choose()
  
  def rectangle (self):
    print("enter the following value for line coordinates")

    x1, y1 = int (input("enter x1 - ")), int (input("enter y1 - "))
    x2, y2 = int (input("enter x2 - ")), int (input("enter y2 - "))
    self.pt1 = (x1, y1)
    self.pt2 = (x2, y2)

    cv2.rectangle(self.image, self.pt1, self.pt2, self.color, self.thickness)
    cv2.imshow("with line image", self.image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    print("for save the image write yes or no")
    option = input("enter here - ")

    if option.lower() == "yes":
      self.save()
    else :
      self.choose()

# function to save 
  def save(self):
    saved = cv2.imwrite("saved.jpg", self.image)
    if saved:
      print("file saved successfully! ")
    else :
      print("file is not saved try again! ")

c1 = Drawing()