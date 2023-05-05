import cv2
import os
import numpy as np
from easy.ImagePyTextDetector import funti
# Load the video file
cap = cv2.VideoCapture('video6.mp4')
count=0
# Loop through each frame of the video
while True:
    # Read a frame from the video
    ret, frame = cap.read()
    if not ret:
        break
    
    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Apply Canny edge detection
    edges = cv2.Canny(gray, 50, 150)
    
    # Find contours in the edge image
    contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Loop through each contour and check if it is a license plate
    for cnt in contours:
        # Get the perimeter of the contour
        perimeter = cv2.arcLength(cnt, True)
        
        # Approximate the contour with a polygon
        approx = cv2.approxPolyDP(cnt, 0.05 * perimeter, True)
        
        # Check if the polygon has four sides and is large enough to be a license plate
        if len(approx) == 4 and cv2.contourArea(approx) > 5000:
            # Extract the license plate image
            x, y, w, h = cv2.boundingRect(cnt)
            plate_img = frame[y:y+h, x:x+w]
            count+=1
            # Save the license plate image
            cv2.imwrite('imge/image{}.jpg'.format(count), plate_img)
    
    # Display the frame with detected license plates
    cv2.resize(frame,(1280,720),fx=0,fy=0, interpolation = cv2.INTER_CUBIC)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close all windows

cap.release()
cv2.destroyAllWindows()
print(funti())
