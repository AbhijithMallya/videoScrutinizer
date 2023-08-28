from flask import Flask, flash, request, redirect, url_for, render_template,Response
import os
import cv2
import numpy as np
from werkzeug.utils import secure_filename

app = Flask(__name__)
camera = cv2.VideoCapture(0)

UPLOAD_FOLDER = 'static/uploads/'
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def gen_frames():  
    while True:
        success, frame = camera.read()  # read the camera frame
        if not success:
            break
        else:
            detector=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
            faces=detector.detectMultiScale(frame,1.1,7)
             #Draw the rectangle around each face
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def image_resize(file):
    image = cv2.imdecode(np.fromstring(file.read(), np.uint8), cv2.IMREAD_COLOR)
    resized_image = cv2.resize(image, (300, 300))
    return resized_image

@app.route('/')
# def home():
#     return render_template('index.html')
def upload_image():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No image selected for uploading')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        resized_image = image_resize(file)
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        cv2.imwrite(file_path, resized_image)
        flash('Image successfully uploaded and displayed below')
        return render_template('index.html', filename=filename)
    else:
        flash('Allowed image types are - png, jpg, jpeg, gif')
        return redirect(request.url)
    
@app.route('/video_feed', methods=['POST'])
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run()
