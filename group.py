"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

my_group = {
    "Jill": {
        "age": 26,
        "job": "Biologist",
        "relations": [
            {"person": "Zalika", "type": "friend"},
            {"person": "John", "type": "partner"}
        ]
    },

    "Zalika": {
        "age": 28,
        "job": "Artist",
        "relations": [
            {"person": "Jill", "type": "friend"}
        ]
    },

    "John": {
        "age": 27,
        "job": "Writer",
        "relations": [
            {"person": "Jill", "type": "partner"}
        ]
    },

    "Nash": {
        "age": 34,
        "job": "Chef",
        "relations": [
            {"person": "John", "type": "cousin"},
            {"person": "Zalika", "type": "landlord"}
        ]
    }
}


# 1. Maximum age of people in the group
max_age = max([
    person["age"]
    for person in my_group.values()
])
print("Maximum age:", max_age)


# 2. Average number of relations per person
average_relations = sum([
    len(person["relations"])
    for person in my_group.values()
]) / len(my_group)

print("Average number of relations:", average_relations)


# 3. Maximum age of people who have at least one relation
max_age_with_relations = max([
    person["age"]
    for person in my_group.values()
    if person["relations"]
])

print("Maximum age with at least one relation:", max_age_with_relations)


# 4. Maximum age of people who have at least one friend
max_age_with_friends = max([
    my_group[name]["age"]
    for name, person in my_group.items()
    if any(
        relation["type"] == "friend"
        for relation in person["relations"]
    )
])

print("Maximum age with at least one friend:", max_age_with_friends)


