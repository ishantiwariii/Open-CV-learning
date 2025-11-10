import cv2

face_cascade = cv2.CascadeClassifier(r"D:\open CV\detection\haarcascade_frontalface_default.xml")

cap = cv2.VideoCapture(0)

while True:
  ret , frame = cap.read()

  grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

  faces = face_cascade.detectMultiScale(grey, 1.1, 5)

  for (x, y, w, h) in faces:
    cv2.rectangle(frame, (x,y), (x+w , y+h), (0,0, 255))
  
  cv2.imshow("video detection", frame)

  if cv2.waitKey(1) & 0xFF == ord("q"):
    break

cap.release()
cv2.destroyAllWindows()