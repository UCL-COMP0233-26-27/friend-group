class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.relationships = {}
        
    def __str__(self):
        if len(self.relationships.keys):
            return f"Person named {self.name}, who is age {self.age}, with relationships: {self.relationships}"
        return f"Person named {self.name}, who is age {self.age}, with no relationships."
    
    def add_relation(self, person, relationship):
        self.relationships[person] = relationship
