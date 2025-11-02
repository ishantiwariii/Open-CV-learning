import cv2

class Convert :
  def __init__(self, location="", image="", grey=None):
    self.path = location
    self.image= image
    self.grey_image = grey

    print("hey there wassup ! ")
    self.loc()

# function to choose location 
  def loc (self):
    self.path = input("enter the path of the image ! ")
    self.image = cv2.imread(self.path)
    if self.image is not None:
      print("the image is successfully loaded")
      self.grey_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
      self.choose()
    else:
      print("image is not loaded successfully, Retry!")
      self.loc()

# function to choose options 
  def choose(self):
    print(""" select 1 for show the greyscale image
              select 2 for save the image  """)
    option = int(input("enter the option here ! "))
    if option == 1 :
      self.greyscale()

    elif option == 2 :
      self.save()
      
    else:
      print("Not a valid option")
 
 # showing greyscale image
  def greyscale(self):
    cv2.imshow("grey scaled color", self.grey_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    op = input("want to save this answer in yes or no - ")

    if op.lower() == "yes":
      self.save()

    elif op.lower() == "no":
      print("Image is not being saved")

    else : 
      print("Failed! option denied")

# function to save the image
  def save(self):
    output = cv2.imwrite("grey_image.jpg", self.grey_image )
    if output:
      print("saved successfully!")

    else : 
      print("Not saved successfully retry ! ")


ishan = Convert()