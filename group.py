"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...
"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...


Jill = {"name": "Jill",
        "age": 26,
        "job": "Biologist",
        "connections":[{"name": "Zalika", "status": "friend"},
        {"name":"John", "status":"partner"}]}


Zalika = {"name": "Zalika",
        "age": 28,
        "job": "Artist",
        "connections":[{"name": "Jill", "status": "friend"}]}


John = {"name": "John",
        "age": 27,
        "job": "Writer",
        "connections":[{"name": "Jill", "status": "partner"}]}

Nash = {"name": "Nash",
        "age": 34,
        "job": "Chef",
        "connections":[{"name": "John", "status": "cousin"},{"name":"Zalika", "status":"tenant"}]}

people = [Jill, Zalika, John, Nash]


#The maximum age of people in the group
max_age = max([person["age"] for person in people])
print(f"The maximum age in the group is {max_age}")


#the average (mean) number of relations among members of the group
relation_number = 0
for person in people:
    relation_number += len(person["connections"])/len(person)
print(f"The mean number of relations is {relation_number}")


#the maximum age of people in the group that have at least one relation
max_age2 = max([person["age"]
    for person in people
        if len(person["connections"]) >= 1])
print(f"The max age of people with at least one relative is {max_age2}")