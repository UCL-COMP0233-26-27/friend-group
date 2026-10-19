"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

class Person:
    def __init__(self, name, age, occupation, relationships=None):
        self.name = name
        self.age = age
        self.occupation = occupation
        self.relationships = relationships

class Relationship:
    def __init__(self, personOne, personTwo, relationshipType):
        self.personOne = personOne
        self.personTwo = personTwo
        self.relationType = self.relationType

jill = Person("Jill", 26, "biologist")
print(f"{jill.name}: {jill.age} years old, {jill.occupation}")

#my_group =
