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
