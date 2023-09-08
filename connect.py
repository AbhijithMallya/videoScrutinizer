# import cv2

# # Replace with your IP camera URL (including username and password)
# camera_url = "http://192.168.2.1/cgi-bin/snapshot.cgi?chn=0&u=karthik&p=Admin_123&.mjpg"

# # Create a VideoCapture object
# cap = cv2.VideoCapture(camera_url)

# if not cap.isOpened():
#     print("Error: Could not connect to the camera.")
#     exit()

# while True:
#     ret, frame = cap.read()

#     if not ret:
#         print("Error: Could not read frame.")
#         break

#     # Perform image processing or analysis on 'frame' here
#     # Display the frame
#     cv2.imshow("IP Camera Stream", frame)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()


# import urllib.request  # Corrected import statement
# import cv2
# import numpy as np

# url = 'http://192.168.2.1/cgi-bin/snapshot.cgi?chn=0&u=karthik&p=Admin_123&.mjpg'

# while True:
#     imageResp = urllib.request.urlopen(url)  # Use urllib.request
#     imgNP = np.array(bytearray(imageResp.read()), dtype=np.uint8)
#     img = cv2.imdecode(imgNP, -1)
#     cv2.imshow("test", img)
#     if ord('q') == cv2.waitKey(10):
#         exit(0)

import cv2

# Define the camera's IP address and credentials
camera_ip = "192.168.2.1"
username = "karthik"
password = "Admin_123"

# Define the URL for the MJPEG stream
stream_url = "rtsp://admin:Admin@123@192.168.2.3:554"

# Create a VideoCapture object
cap = cv2.VideoCapture(stream_url)

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (1220, 480), fx = 0.1, fy = 0.1)
    # frame = frame.resize(500,500,frame)

    if not ret:
        print("Error reading frame")
        break

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
