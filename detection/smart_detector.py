import cv2

face_cascade = cv2.CascadeClassifier(r"D:\open CV\detection\haarcascade_frontalface_default.xml")
smile_cascade = cv2.CascadeClassifier(r"D:\open CV\detection\haarcascade_smile.xml")
eyes_cascade = cv2.CascadeClassifier(r"D:\open CV\detection\haarcascade_eye.xml")

cap = cv2.VideoCapture(0)

while True:
  ret , frame = cap.read()

  grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

  faces = face_cascade.detectMultiScale(grey, 1.1, 5)

  for (x, y, w, h) in faces:
    cv2.rectangle(frame, (x,y), (x+w , y+h), (0,0, 255))
  
    roi_gray = grey[y:y+h, x:x+w]
    roi_color = frame[y:y+h, x:x+w]
  

    eye = eyes_cascade.detectMultiScale(roi_gray, 1.3, 5)
    if len(eye) > 0 :
      cv2.putText(frame, "Eyes detected", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX,0.6, (255, 0 , 0 ), 3)
      
    smile = smile_cascade.detectMultiScale(roi_gray, 1.8, 25)
    if len(smile) > 0 :
      cv2.putText(frame, "smile detected", (x, y-30), cv2.FONT_HERSHEY_SIMPLEX,0.6, (255, 0 , 0 ), 3)
  cv2.imshow("video detection", frame)

  if cv2.waitKey(1) & 0xFF == ord("q"):
    break

cap.release()
cv2.destroyAllWindows()