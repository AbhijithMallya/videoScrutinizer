import face_recognition
import os

# Directory containing the face images
def getFaceEncodings(folderName):

    image_directory = folderName + "/"

    # Initialize empty lists for face encodings and names
    known_face_encodings = []
    known_face_names = []

    # Iterate through the files in the image directory
    for filename in os.listdir(image_directory):
        if filename.endswith(".jpg"):
            # Load the image
            image_path = os.path.join(image_directory, filename)
            image = face_recognition.load_image_file(image_path)

            # Encode the face
            face_encoding = face_recognition.face_encodings(image)[0]

            # Extract the name from the filename (assuming the filename is in the format "name.jpg")
            name = os.path.splitext(filename)[0]

            # Append the encoding and name to the respective lists
            known_face_encodings.append(face_encoding)
            known_face_names.append(name)
    return known_face_encodings , known_face_names
