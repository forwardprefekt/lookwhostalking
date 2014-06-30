import numpy as np
import cv2
import time
import serial


ser = serial.Serial('/dev/ttyACM0', 9600)

cap = cv2.VideoCapture(0)

cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")

x = 1 


def box(rects, img):
    for x1, y1, x2, y2 in rects:
        cv2.rectangle(img, (x1, y1), (x2, y2), (127, 255, 0), 2)
    #cv2.imwrite('/vagrant/img/detected.jpg', img);
	return img


showbox = 0

while(True):
    x = x+1
    # Capture frame-by-frame
    ret, frame = cap.read()
    if (x > 5):
	x = 0 
    	rects = cascade.detectMultiScale(frame, 1.3, 4, cv2.cv.CV_HAAR_SCALE_IMAGE, (20,20))
    	if len(rects) > 0:
    		curpos = rects[0,0]
		if (curpos < 220):
			ser.write('m')
			print "m"
		if (curpos > 280):
			ser.write('p')
			print "p"
		

    		print rects[0,0]
		if (showbox == 1):
			frame = box(rects, frame)
    
    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    if cv2.waitKey(1) & 0xFF == ord('d'):
	print "showing rects"
	showbox = 1

    # Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
