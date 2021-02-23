# This code is used to scan an image and gather the locations of each face that is recognized as a face (known or unknown).
import face_recognition
from imagelocations import known_images, unknown_images, group_images

def find_faces():
    # Current image selected by index.
    current_image_index = 3
    # Get image and store data in image variable.
    image = face_recognition.load_image_file(group_images[current_image_index])
    # Get location of every face recognized in selected image.
    face_locations = face_recognition.face_locations(image)
    # Print array of coordinates for each face.
    # print(face_locations)
    # Print how many faces there are in selected image.
    print(f"There are {len(face_locations)} faces recognized in the selected image.")
find_faces()
