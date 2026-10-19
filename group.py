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
