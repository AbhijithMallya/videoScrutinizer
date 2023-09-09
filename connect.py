
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




# import cv2

# # Define the camera's IP address and credentials
# # camera_ip = "192.168.2.1"
# # username = "karthik"
# # password = "Admin_123"

# # Define the URL for the MJPEG stream
# stream_url = "rtsp://admin:Admin@123@192.168.2.1:554"
# cap = cv2.VideoCapture(stream_url)

# while True:
#     ret, frame = cap.read()
#     frame = cv2.resize(frame, (1220, 480), fx = 0.1, fy = 0.1)
#     # frame = frame.resize(500,500,frame)

#     if not ret:
#         print("Error reading frame")
#         break

#     cv2.imshow('frame', frame)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()









import cv2
import threading

# Define the stream URLs for your CCTV cameras
stream_urls = [
    "rtsp://admin:Admin@123@192.168.2.1:554",
    "rtsp://admin:Admin@123@192.168.2.2:554",
    "rtsp://admin:Admin@123@192.168.2.3:554",
    # Add the URLs for your other cameras here
]

# Create a list to store VideoCapture objects
capture_objects = []

# Create VideoCapture objects for each stream URL
for url in stream_urls:
    cap = cv2.VideoCapture(url)
    capture_objects.append(cap)

# Function to read and display frames from a VideoCapture object
def display_camera_stream(cap, window_name):
    while True:
        ret, frame = cap.read()
        if not ret:
            print(f"Error reading frame from {window_name}")
            break

        # Resize the frame if needed
        frame = cv2.resize(frame, (1220, 480), fx = 0.1, fy = 0.1)

        cv2.imshow(window_name, frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Create threads for each camera stream
threads = []
for i, cap in enumerate(capture_objects):
    window_name = f'Camera {i + 1}'
    thread = threading.Thread(target=display_camera_stream, args=(cap, window_name))
    threads.append(thread)

# Start the threads to display camera streams
for thread in threads:
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()

# Release VideoCapture objects and close OpenCV windows
for cap in capture_objects:
    cap.release()
cv2.destroyAllWindows()



# import cv2

# # Define the URLs for the MJPEG streams of multiple cameras
# stream_urls = [
#     "rtsp://admin:Admin@123@192.168.2.1:554",
#     "rtsp://admin:Admin@123@192.168.2.2:554"
#     # Add more stream URLs for additional cameras here
# ]

# # Create a list to store VideoCapture objects
# capture_objects = []

# # Create VideoCapture objects for each stream URL
# for url in stream_urls:
#     cap = cv2.VideoCapture(url)
#     capture_objects.append(cap)

# while True:
#     frames = []  # To store frames from all cameras

#     # Read frames from each camera
#     for cap in capture_objects:
#         ret, frame = cap.read()
#         if not ret:
#             print(f"Error reading frame from {cap}")
#             continue

#         # Resize each frame if needed
#         frame = cv2.resize(frame, (1220, 480), fx=0.1, fy=0.1)

#         frames.append(frame)

#     # Display frames from all cameras side by side
#     if len(frames) > 0:
#         stacked_frames = cv2.hconcat(frames)
#         cv2.imshow('Multiple Camera Streams', stacked_frames)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # Release VideoCapture objects and close OpenCV windows
# for cap in capture_objects:
#     cap.release()
# cv2.destroyAllWindows()
