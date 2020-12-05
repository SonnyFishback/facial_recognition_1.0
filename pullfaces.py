from PIL import Image
import face_recognition
from imagelocations import known_images, unknown_images, group_images

# Get image and store data in image variable.
image = face_recognition.load_image_file("./images/groups/sonnyAndGroup.PNG")
# Get location of every face recognized in selected image.
face_locations = face_recognition.face_locations(image)
# Loop through each face location.
for each_face_location in face_locations:
    top, right, bottom, left =  each_face_location
    face_image = image[top:bottom, left:right]
    pil_image = Image.fromarray(face_image) 
    # Show saved image in default image viewer.
    pil_image.show()
    # Save image with the file name of "the top coordinate" + ".jpg".
    # pil_image.save(f"{top}.jpg")
