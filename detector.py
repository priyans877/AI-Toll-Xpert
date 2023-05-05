import cv2
import numpy as np
import pytesseract
import os
import sys
import imutils

from easy.DetectorPyOcr import funti

b=[]
# Load the video
url="http://192.168.216.49:4747/video"
cap = cv2.VideoCapture("video5.mp4")

# Create an edge detector
edge_detector = cv2.Canny

# Create a contour detector
if cv2.__version__.startswith('4'):
    contour_detector = cv2.findContours
else:
    _, contour_detector = cv2.findContours

count=0
# Loop through each frame in the video
while cap.isOpened():
    # Read the frame
    ret, image = cap.read()

    # If the frame is not read correctly, break the loop
    if not ret:
        break
    fps = cap.get(40)
    image=imutils.resize(image,width = 960)
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply edge detection
    edges = edge_detector(gray, 100, 200)

    # Find contours
    contours, _ = contour_detector(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Filter out small contours
    contours = [c for c in contours if cv2.contourArea(c) > 1000]

    #the largest area, if any contours are found
    if contours:
        max_contour = max(contours, key=cv2.contourArea)

        # mask for the license plate
        mask = np.zeros_like(gray)
        cv2.drawContours(mask, [max_contour], 0, 255, -1)

        #to extract the license plate
        plate = cv2.bitwise_and(image, image, mask=mask)
    
        i=1
        if i==1:
            max_contour = max(contours, key=cv2.contourArea)
            count+=1
            #largest contour
            x, y, w, h = cv2.boundingRect(max_contour)
            r,frame=cap.read()
            # Crop image rectangle
            cropped = plate[y:y+h, x:x+w]
            #cv2.imshow('video2',frame)
            # result image
            cv2.imshow('License Plate Extraction', cropped)
            cv2.imwrite("car.jpg",cropped)
            #tex=pytesseract.image_to_string(cropped, lang='eng').strip()
            tex=funti(cropped)
            b.append(tex)
            #print(type(tex))
            if len(tex)!=0:
                for item in tex:
                    for i in range(1,len(item)-1):
                        print(item[i])
                        print(len(item[i]))
                        print("*---------------------------------*--------------------------------*")


            

    # Wait for a key press to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):   
        '''print(b) 
        for item in b:
            print(item[1])
            print("*-------------------------------------*----------------------------------------*")'''
        break

# Release the video capture and close all windows
cap.release()
cv2.destroyAllWindows()



