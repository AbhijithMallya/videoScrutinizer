import cv2

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