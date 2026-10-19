"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

group = {
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


# Task 1: Maximum age
max_age = max([person["age"] for person in group.values()])
print("Maximum age:", max_age)


# Task 2: Average number of relations
avg_relations = sum(
    [len(person["relations"]) for person in group.values()]
) / len(group)
print("Average number of relations:", avg_relations)


# Task 3: Maximum age of people with relations
max_age_with_relations = max(
    [person["age"] for person in group.values()
     if len(person["relations"]) > 0],
    default=None
)
print("Maximum age with relations:", max_age_with_relations)


# Task 4: Maximum age of people with a friend
max_age_with_friend = max(
    [person["age"] for person in group.values()
     if any(relation["type"] == "friend"
            for relation in person["relations"])],
    default=None
)
print("Maximum age with a friend:", max_age_with_friend)


