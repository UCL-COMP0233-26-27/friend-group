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

max_age = max(person["age"] for person in people)
mean_connections = sum(len(person["connections"]) for person in people) / len(people)
max_age_with_friend = max(
    person["age"]
    for person in people
    if any(
        connection["status"] == "friend"
        for connection in person["connections"]
    )
)
max_age_with_at_least_1_connections = max(person["age"] for person in people if len(person["connections"]) >= 1)

print (max_age)
print (mean_connections)
print (max_age_with_friend)
print (max_age_with_at_least_1_connections)
