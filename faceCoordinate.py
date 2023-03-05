from __future__ import print_function
import cv2 as cv
import argparse
def detectAndDisplay(frame):
    frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    frame_gray = cv.equalizeHist(frame_gray)
    #-- Detect faces
    faces = face_cascade.detectMultiScale(frame_gray)
    for (x,y,w,h) in faces:
        center = (x + w//2, y + h//2)
        frame = cv.ellipse(frame, center, (w//2, h//2), 0, 0, 360, (255, 0, 255), 4)
        faceROI = frame_gray[y:y+h,x:x+w]

            # Capture frames in the video
        #ret, frame = cap.read()
    
        # describe the type of font
        # to be used.
        font = cv.FONT_HERSHEY_SIMPLEX
    
        # Use putText() method for
        # inserting text on video
        cv.putText(frame, 
                    str(center), 
                    (50, 50), 
                    font, 1, 
                    (0, 255, 255), 
                    2, 
                    cv.LINE_4)
    
        # Display the resulting frame
        #cv.imshow('video', frame)

        #-- In each face, detect eyes
        eyes = eye_cascade.detectMultiScale(faceROI)
        for (x2,y2,w2,h2) in eyes:
            eye_center = (x + x2 + w2//2, y + y2 + h2//2)
            radius = int(round((w2 + h2)*0.25))
            frame = cv.circle(frame, eye_center, radius, (255, 0, 0 ), 4)
    cv.imshow('Capture - Face detection', frame)
face_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_eye.xml')
#-- 1. Load the cascades
if not face_cascade.load(cv.samples.findFile(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')):
    print('--(!)Error loading face cascade')
    exit(0)
if not eye_cascade.load(cv.samples.findFile(cv.data.haarcascades + 'haarcascade_eye.xml')):
    print('--(!)Error loading eyes cascade')
    exit(0)

#-- 2. Read the video stream
cap = cv.VideoCapture(1)
if not cap.isOpened:
    print('--(!)Error opening video capture')
    exit(0)
while True:
    ret, frame = cap.read()
    if frame is None:
        print('--(!) No captured frame -- Break!')
        break

    detectAndDisplay(frame)
    if cv.waitKey(1) == ord(" "):
        break