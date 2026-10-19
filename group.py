"""An example of how to represent a group of acquaintances in Python."""

my_group = [
    {
        "name": "Jill",
        "age": 26,
        "job": "biologist",
        "connections": [
            {"person": "Zalika", "relationship": "friend"},
            {"person": "John", "relationship": "partner"},
        ],
    },
    {
        "name": "Zalika",
        "age": 28,
        "job": "artist",
        "connections": [
            {"person": "Jill", "relationship": "friend"},
        ],
    },
    {
        "name": "John",
        "age": 27,
        "job": "writer",
        "connections": [
            {"person": "Jill", "relationship": "partner"},
        ],
    },
    {
        "name": "Nash",
        "age": 34,
        "job": "chef",
        "connections": [
            {"person": "John", "relationship": "cousin"},
            {"person": "Zalika", "relationship": "landlord"},
        ],
    },
]# Your code to go here...
# A person without a job can have job set to None.
# A person without connections can have an empty connections list.
# Relationships are directional; reverse connections must be added explicitly.
# Each relationship describes this person's role relative to the named person.
def forget(group, person1, person2):
    for person in group:
        if person["name"] == person1:
            other_person = person2
        elif person["name"] == person2:
            other_person = person1
        else:
            continue

        remaining_connections = []

        for connection in person["connections"]:
            if connection["person"] != other_person:
                remaining_connections.append(connection)

        person["connections"] = remaining_connections

def add_person(group, name, age, job=None, relations=None):
    """Add a person, rejecting duplicate names."""
    for person in group:
        if person["name"] == name:
            raise ValueError("A person with this name already exists.")

    group.append({
        "name": name,
        "age": age,
        "job": job,
        "connections": [
            dict(connection) for connection in relations
        ] if relations is not None else [],
    })


def average_age(group):
    """Return the average age, or None for an empty group."""
    if not group:
        return None

    total_age = 0
    for person in group:
        total_age += person["age"]

    return total_age / len(group)

