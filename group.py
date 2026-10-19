"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

# my_group = 

class Person:
    def __init__(self, name, age, occupation=None):
        self.name = name
        self.age = age
        self.occupation = occupation
        self.relationships = {}

    def add_relationship(self, realted_person, relation):
        self.relationships.update({realted_person: relation})


person0 = Person("Jill", 26, "biologist")
person1 = Person("Zalika", 28, "artist")
person2 = Person("John", 27, "writer")
person3 = Person("Nash", 34, "chef")

my_group = [person0, person1, person2, person3]

person0.add_relationship(person1, "friend")

