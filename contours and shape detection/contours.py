import cv2 

image = cv2.imread(r"D:\open CV\pic\2D-Shapes-06.png")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

_ , frame = cv2.threshold(gray, 100, 250  ,cv2.THRESH_BINARY)

# find countours 
# learn the syntaxes too 

contours , hierarchy = cv2.findContours(frame,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(image, contours, -1, (0,255,0), 3)


cv2.imshow("contours", image)

cv2.waitKey(0)
cv2.destroyAllWindows()





# here we take a note about how to do contour analysis
'''
first we will read the image 
then we will convert the image using cv2.cvtcolor
and then we will make the image in binary form that is also known as black nd white 
and then we will call the cv2.findcontours and then pass the values in the syntax , here we pass the binary image 
and then we use cv2.drawcontours to draw the countour on thee image and here we use the original image 
and then we call cv2.imshow and then waitkey and then destroy all window 
that's it.........

'''