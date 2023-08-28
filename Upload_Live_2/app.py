from flask import Flask, render_template, request, Response
import cv2
import face_recognition
import numpy as np

app = Flask(__name__)

cap = cv2.VideoCapture(0)
known_face_encodings = []
known_face_labels = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        uploaded_file = request.files['image']
        uploaded_label = request.form['label']

        if uploaded_file:
            uploaded_image = face_recognition.load_image_file(uploaded_file)
            uploaded_face_encoding = face_recognition.face_encodings(uploaded_image)[0]
            known_face_encodings.append(uploaded_face_encoding)
            known_face_labels.append(uploaded_label)

    return render_template('index.html')

def generate_frames():
    while True:
        ret, frame = cap.read()

        if not ret:
            break

        rgb_frame = frame[:, :, ::-1]

        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

            name = "Unknown"

            if True in matches:
                matched_indices = [i for i, match in enumerate(matches) if match]
                for index in matched_indices:
                    name = known_face_labels[index]
                    cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
                    font = cv2.FONT_HERSHEY_DUPLEX
                    cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)

        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)
