from flask import Flask, render_template, request, Response
import cv2
import numpy as np
import csv , datetime , time
from dataExtraction import getFaceEncodings
import face_recognition
from csvWriter import writeCsv
app = Flask(__name__)

#Initialize the video Streams
video_capture = cv2.VideoCapture(0)


#CSV File initialization
csv_file = open("recognized_detections.csv", "a", newline="")
csv_writer = csv.   writer(csv_file)
csv_writer.writerow(["Name", "Timestamp"])
last_detection_time = time.time()

#Get facial Encoding from the Folder --> faceImages
known_face_encodings , known_face_names = getFaceEncodings('faceImages')

# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True



@app.route('/' )
def index():
    return render_template('index.html')

def generate_frames():
    while True:
        ret ,frame = video_capture.read()
        process_this_frame = True
    # Only process every other frame of video to save time
        if process_this_frame:
            # Resize frame of video to 1/4 size for faster face recognition processing
            small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25) #change to 0.25 for faster recognition

            # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
            rgb_small_frame = small_frame[:, :, ::-1]
            
            # Find all the faces and face encodings in the current frame of video
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

            face_names = []
            for face_encoding in face_encodings:
                # See if the face is a match for the known face(s)
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                name = "Unknown"

                face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = known_face_names[best_match_index]

                face_names.append(name)

        process_this_frame = not process_this_frame


        # Display the results
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            # Scale back up face locations since the frame we detected in was scaled to 1/4 size
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            # Draw a box around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
            # Draw a label with a name below the face
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)


    ###================   CSV READER START===============
            if name != "Unknown":

                # Get the current timestamp
                timestamp = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")

                # Check if enough time (30 seconds) has passed since the last detection
                current_time = time.time()
                if current_time - last_detection_time >= 30:
                    # Write the detection to the CSV file
                    csv_writer.writerow([name, timestamp])
                    last_detection_time = current_time
                
            #writeCsv(name=name , last_detection_time=last_detection_time, csv_writer= csv_writer)
    ###================   CSV READER END===============
        
        #recieveFrame(frame)
        # Display the resulting image
        #cv2.imshow('Video',frame)
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)
