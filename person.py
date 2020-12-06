# This will represent each face and store information to create a new "person" for each existing face and new face that is found.
class Person:
    def __init__(self, persons_name, image_of_person, location_of_face, encodings, facial_features ):
        self.persons_name = persons_name
        self.image_of_person = image_of_person
        self.location_of_face = location_of_face
        self.encodings = encodings
        self.facial_features = facial_features

