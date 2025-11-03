import cv2 

cap =  cv2.VideoCapture(0)
# we pass 0 if webcam is of pc 
# we pass 1 if webcam is external

while True:
  ret, frame = cap.read()# return true or false to ret and frames to frame 

  if not ret:
    print("could not read frame")
    break

  cv2.imshow("webcam Feed", frame)
  
  if cv2.waitKey(1) & 0xFF == ord('q'):
    print("Quiting.........")
    break

cap.release()
cv2.destroyAllWindows()