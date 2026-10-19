"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

class Person:
    def __init__(self, name, age, occupation=None, relationships=[]):
        self.name = name
        self.age = age
        self.occupation = occupation
        self.relationships = relationships

class Relationship:
    def __init__(self, personOne, personTwo, relationshipType):
        self.personOne = personOne
        self.personTwo = personTwo
        self.relationshipType = relationshipType

jill = Person("Jill", 26, "biologist")
zalika = Person("Zalika", 28, "artist")
john = Person("John", 27, "writer")
nash = Person("Nash", 34, "chef")

rltn_j_z = Relationship(jill, zalika, "friend")

jill.relationships.append(rltn_j_z)



print(f"{jill.name}: {jill.age} years old, {jill.occupation}, {jill.relationships[0]}")

#my_group =
