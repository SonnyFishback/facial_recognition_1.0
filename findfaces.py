# This code is used to scan an image and gather the locations of each face that is recognized as a face (known or unknown).
import face_recognition

image = face_recognition.load_image_file("./images/groups/sonnyAndGroup.PNG")
# Get location of every face recognized in selected image.
face_locations = face_recognition.face_locations(image)
# Print array of coordinates for each face.
# print(face_locations)
# Print how many faces there are in selected image.
print(f"There are {len(face_locations)} faces recognized in the selected image.")

