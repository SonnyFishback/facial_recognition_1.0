import face_recognition
from imagelocations import known_images, unknown_images, group_images

def find_match():
    # Current known image selected by index.
    current_known_image_index = 0
    # Current unknown image selected by index.
    current_unknown_image_index = 1
    # Get known image and store data in current_known_image variable.
    current_known_image = face_recognition.load_image_file(known_images[current_known_image_index])
    # Get known image engonding data and store it in variable current_known_image_encodings.
    current_known_image_encodings = face_recognition.face_encodings(current_known_image)[0]
    # Get unknown image and store data in current_unknown_image variable.
    current_unknown_image = face_recognition.load_image_file(unknown_images[current_unknown_image_index])
    # Get known image engonding data and store it in variable current_unknown_image_encodings.
    current_unknown_image_encodings = face_recognition.face_encodings(current_unknown_image)[0]
    # print(current_known_image_encodings[0], current_unknown_image_encodings[0])

    results = face_recognition.compare_faces([current_known_image_encodings], current_unknown_image_encodings)

    if results[0]:
        print("It's a match!")
    else:
        print("It's not a match!")

find_match( )
