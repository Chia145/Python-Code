import cv2
import time
import numpy

# Start the video capture
video = cv2.VideoCapture(0) 
# Read the image having black bg
image = cv2.imread("pic.jpeg") 

while True:
    # Reading the frames of the video
    ret, frame = video.read()
    # Resizing the image and the video 
    frame = cv2.resize(frame, (640, 480)) 
    image = cv2.resize(image, (640, 480))
    # Saving the shades of black 
    upperBlack = np.array([104,153,70])
    lowerBlack = np.array([30,30,0])
    # Creating a mask
    mask = cv2.inRange(frame, upperBlack, lowerBlack)
    res = cv2,bitwise_and(frame, frame, mask = mask)
    # Returning image if f = 0
    frame2 = frame - res
    frame2 = np.where(frame2 == 0, image, frame2) 
    # Show the real and the masked video
    cv2.imshow("video", frame)
    cv2.imshow("mask", frame2)
    # Breaking the loop if the user presses Escape key
    if cv2.waitkey(1) & 0xFF == ord('q'):
        break

# Realeasing the video 
video.realese()
# Destroying all the windows
cv2.destroyAllWindows()