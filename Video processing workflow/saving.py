import cv2

camera = cv2.VideoCapture(0)

frame_width = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height= int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))

codec = cv2.VideoWriter_fourcc(*'XVID')
recorded = cv2.VideoWriter("my_video.mp4", codec, 20, (frame_width, frame_height))

while True:
  success , image = camera.read()

  if not success:
    break

  recorded.write(image)
  cv2.imshow("live camera feed", image)

  if cv2.waitKey(1) & 0xFF == ord('q'):
    print("Quitting...........")
    break

camera.release()
recorded.release()
cv2.destroyAllWindows()


# major notes 

# cv2.VideoCapture(0) means “open the default webcam.”
# - 0 refers to your first (default) camera.
# - If you had multiple cameras, you’d use 1, 2, etc.



# frame_width = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
# frame_height = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))
# These lines read your camera’s frame width and height (like 640×480 or 1280×720).
# It’s needed so that your video file is saved at the same resolution.

# codec = cv2.VideoWriter_fourcc(*'XVID')
# recorded = cv2.VideoWriter("my_video.mp4", codec, 20, (frame_width, frame_height))
# This tells OpenCV how to save the video:

# - 'XVID' → the video compression format (codec).
# - "my_video.mp4" → the output file name.
# - 20 → the frames per second (FPS).
# - (frame_width, frame_height) → the size of each video frame.

# while True:
#     success, image = camera.read()

# - This reads one frame from the webcam at a time.
# - success tells whether the frame was captured properly (True/False).
# - image is the actual frame (a NumPy array).

# recorded.write(image)
# cv2.imshow("live camera feed", image)
# - recorded.write(image) saves each captured frame into the video file.
# - cv2.imshow() shows the live feed window on your screen.

# if cv2.waitKey(1) & 0xFF == ord('q'):
#     print("Quitting...........")
#     break

# - This waits for 1 millisecond for a key press.
# - If the user presses the letter ‘q’, the program stops recording.


# camera.release()
# recorded.release()
# cv2.destroyAllWindows()

# - Frees your webcam.
# - Finishes writing the video file.
# - Closes any OpenCV windows.