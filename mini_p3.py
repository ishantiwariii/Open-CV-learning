# To make a program which takes input from user like - 
# want to start webcam 
# want to record and save the vdo 
# also can select the name to save files 


# here is the workflow 
# first make the class web_server
# make a constructor and give some values 
# make a choose function 
# make a start webcam function 
# make a start webcam with recording function 
# make a function to get name of file if user call the recording function 
# make an object and test it 

import cv2

class Web_serv:
  def __init__(self, name= None):
    self.file_name = name
    print("Hey buddy wassup!")
    self.choose()
  
  def choose (self):
    print("""here are some option to start the functions! 
              CHOOSE 1 for starting web cam
              CHOOSE 2 for starting webcam with recording""")
    option  = int(input("write here - "))
    if option == 1:
      self.cam()
    elif option == 2 : 
      self.recorder_cam()
    else : 
      print("enter a valid option ! ")
      self.choose()
  
  def cam(self):
    camera = cv2.VideoCapture(0)

    while True:
      ret , frame = camera.read()

      if not ret:
        print("something got wrong try again! ")
        break

      cv2.imshow("live video cam", frame)

      if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Quiting......")
        break
      
    camera.release()
    cv2.destroyAllWindows()

  def recorder_cam(self):
    
    camera = cv2.VideoCapture(0)

    frame_width = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))

    codec = cv2.VideoWriter_fourcc(*'mp4v')
    recorder = cv2.VideoWriter("recorded.mp4", codec, 20, (frame_width, frame_height))
    while True:
      ret , frame = camera.read()

      if not ret:
        print("something got wrong try again! ")
        break
      
      recorder.write(frame)
      cv2.imshow("live video cam", frame)
      
      if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Quitting...........")
        break

    camera.release()
    recorder.release()
    cv2.destroyAllWindows()

ishan = Web_serv()