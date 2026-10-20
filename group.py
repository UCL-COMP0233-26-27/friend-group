"""An example of how to represent a group of acquaintances in Python."""

my_group = {
    "Jill":{
        "age": 26,
        "occupation": "biologist",
        "relationships":{
            "friend": "Zalika",
            "partner": "John"
        }
    },

    "Zalika":{
        "age": 28,
        "occupation": "artist",
        "relationships":{
            "friend": "Jill",
            "landlord": "Nash"
        }
    },

    "John":{
        "age": 27,
        "occupation": "writer",
        "relationships":{
            "partner": "Jill",
            "cousin": "Nash"
        }
    },

    "Nash":{
        "age": 34,
        "occupation": "chef",
        "relationships":{
            "cousin": "John",
            "tenant": "Zalika"
        }
    }
}

print(my_group["Jill"])
print(my_group["Jill"]["relationships"]["friend"])  # Output: Zalika

# the maximum age of people in the group

max_age = max( [person["age"] for person in my_group.values()] )
print(max_age)

# the average number of relations among members of the group

group_size = len(my_group)

relationship_count = 0 
for person in my_group.values():
    relationship_count += len(person["relationships"])

avg_ralationships = relationship_count/group_size
print(avg_ralationships)

# Maximum age of people who have at least one relation

person_with1relation = []
for person in my_group.values():
    if len(person["relationships"]) > 0:
        person_with1relation.append(person)

max_age2 = max( [person["age"] for person in person_with1relation] )
print(max_age2)

# Maximum age of people who have at least one friend

person_with1friend = []
for person in my_group.values():
    for relation in person["relationships"]:
        if relation == "friend":
            person_with1friend.append(person)

max_age3 = max( [person["age"] for person in person_with1friend] )
print(max_age3)

