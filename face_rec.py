import face_recognition
import os
import cv2

KNOWN_FACES_DIR = "known_faces"
UNKNOWN_FACES_DIR = "unknown_faces"
TOLERANCE = 0.6
FRAME_THICKNESS = 3
FONT_THICKNESS = 2
MODEL = "cnn" #hog

print("Loading know faces...")

known_faces = []
known_names = []

for name in os.listdir(KNOWN_FACES_DIR):
    for file_name in os.listdir(f"{KNOWN_FACES_DIR}/{name}"):
        image = face_recognition.load_image_file(f"{KNOWN_FACES_DIR}/{name}/{file_name}")
        encoding = face_recognition.face_encodings(image)[0]

        known_faces.append(encoding) 
        known_names.append(name)

print("Processing unknown faces...")

for file_name in os.listdir(UNKNOWN_FACES_DIR):
    print(file_name)
    image = face_recognition.load_image_file(f"{UNKNOWN_FACES_DIR}/{file_name}")
    locations = face_recognition.face_locations(image, MODEL)
    encodings = face_recognition.face_encodings(image, locations)
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    for face_encodings, face_locations in zip(encodings, locations):
        results = face_recognition.compare_faces(known_faces, face_encodings, TOLERANCE )
        match = None
        if True in results:
            match =  known_names[results.index(True)]
            print(f"Match found: {match}")