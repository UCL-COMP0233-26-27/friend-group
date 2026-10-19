"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

class Person: 
    def __init__(self, name):
        self.name = name
        self.age = []
        self.occupation = []
        self.relationships = []

    def add_relationships(self, relationships):
        Relationships = (relationships)
        self.relationships.append(relationships)
        return Relationships

    def add_age(self, age):
        Age = (age)
        self.age.append(age)
        return Age

    def add_occupation(self, occupation):
        Occupation = (occupation)
        self.occupation.append(occupation)
        return Occupation

    def group_sim(self):
        print("{who} is in the group, they are {age} and work as a {occupation} and their " \
        "relationships to others are {relationships}".format(who=self.name, age=self.age, 
                                                             occupation = self.occupation, 
                                                             relationships = self.relationships))

class Group:
    def __init__(self, group):
        self.group = group
        self.members = []

    def add_member(self, member):
        

Jill = Person('Jill')
Jill.add_relationships('Zalikas friend and Johns partner')
Jill.add_age('26')
Jill.add_occupation('biologist')

Jill.group_sim



    


