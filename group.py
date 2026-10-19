"""An example of how to represent a group of acquaintances in Python."""

class Person:
    def __init__(self, name, age, occupation=None):
        self.name = name
        self.age = age
        self.occupation = occupation
        self.connections = {}

    def add_connection(self, relation, other_person, reverse_relation=None):
        if relation not in self.connections:
            self.connections[relation] = []
        self.connections[relation].append(other_person.name)

        if reverse_relation:
            if reverse_relation not in other_person.connections:
                other_person.connections[reverse_relation] = []
            if self.name not in other_person.connections[reverse_relation]:
                other_person.connections[reverse_relation].append(self.name)

Jill = Person('Jill', 26, 'Biologist')
Zalika = Person('Zalika', 28, 'Artist')
John = Person('John', 27, 'Writer')
Nash = Person('Nash', 34, 'Chef')


Jill.add_connection('Friend', Zalika, reverse_relation='Friend')
Jill.add_connection('Partner', John, reverse_relation='Partner')
Zalika.add_connection('Landlord', Nash, reverse_relation='Tenant')
John.add_connection('Cousin', Nash, reverse_relation='Cousin')