
# import modules
import numpy as np

# define class for person object 
class Person:
    def __init__(self, name, age, occupation=None):
        self.name = name
        self.age = age
        self.occupation = occupation
        self.relationships = {}

    def add_relationship(self, related_person, relation):
        self.relationships[related_person] = relation

# create person objects and relationships 
Jill = Person("Jill", 26, "biologist")
Zalika = Person("Zalika", 28, "artist")
John = Person("John", 27, "writer")
Nash = Person("Nash", 34, "chef")

Jill.add_relationship(Zalika, "friend")
Jill.add_relationship(John, "partner")
Zalika.add_relationship(Jill, "friend")
John.add_relationship(Jill, "partner")
Nash.add_relationship(John, "cousin")
Nash.add_relationship(Zalika, "landlord")

my_group = [Jill, Zalika, John, Nash]

# print max age of people in the group 

max_age = max([person.age for person in my_group])
print("max age of people in group:", max_age)

# alternative
#age = 0 
#for person in my_group:
#    if person.age > age:
#        age = person.age
#        oldest_person = person.name
#print("oldest person:", oldest_person, "age:", age)

# mean number of relations of people in the group 

num_relations = np.array([len(person.relationships) for person in my_group ])
mean_relations = np.mean(num_relations)
print("mean number of relations of people in the group:", mean_relations)

# alternative 
# num_relations = []
# for person in my_group:
#    num_relations.append(len(person.relationships)) 
# mean_relations = sum(num_relations)/len(num_relations)
# print(mean_relations)

# max age of people who have one relation

age_1_relation = [int(person.age) for person in my_group if len(person.relationships) >= 1]
max_age_1_relation = max(age_1_relation)
print("max age of people who have at least one relation:", max_age_1_relation)

# max age of people who have one friend
one_friend_list = []
for person in my_group:
    friend_count = 0 
    for relation in person.relationships.values():
        if  relation == "friend":
            friend_count += 1
    if friend_count >= 1:
        one_friend_list.append(person)

max_age_1_friend = max([person.age for person in one_friend_list])
print("max age of people with at least one friend:", max_age_1_friend)
