import cv2
import numpy as np

# Define the URLs for the MJPEG streams of multiple cameras
stream_urls = [
    "rtsp://admin:Admin@123@192.168.2.1:554",
    "rtsp://admin:Admin@123@192.168.2.2:554",
    "rtsp://admin:Admin@123@192.168.2.3:554"  # Add more stream URLs for additional cameras here
]

# Define the desired width and height for the merged frame
merged_frame_width = 550  # Adjust as needed
merged_frame_height = 500  # Adjust as needed

# Create a list to store VideoCapture objects
capture_objects = []

# Create VideoCapture objects for each stream URL
for url in stream_urls:
    cap = cv2.VideoCapture(url)
    capture_objects.append(cap)

while True:
    frames = []  # To store frames from all cameras

    # Read frames from each camera, resize, and store in frames list
    for cap in capture_objects:
        ret, frame = cap.read()
        if not ret:
            print(f"Error reading frame from {cap}")
            continue

        # Resize each frame to the desired dimensions
        frame = cv2.resize(frame, (merged_frame_width, merged_frame_height))

        frames.append(frame)

    # Create a blank merged frame
    merged_frame = np.zeros((merged_frame_height, merged_frame_width * len(frames), 3), dtype=np.uint8)

    # Paste each resized frame onto the merged frame
    for i, frame in enumerate(frames):
        merged_frame[:, i * merged_frame_width:(i + 1) * merged_frame_width, :] = frame

    # Display the merged frame
    cv2.imshow('Merged Camera Streams', merged_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release VideoCapture objects and close OpenCV windows
for cap in capture_objects:
    cap.release()
cv2.destroyAllWindows()
