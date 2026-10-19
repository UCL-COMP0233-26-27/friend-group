"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

my_group = [
    {
        "name": "Jill",
        "age": 26,
        "job": "Biologist",
        "relationships": {
            "Zalika": "friend",
            "John": "partner"
        }
    },
    {
        "name": "Zalika",
        "age": 28,
        "job": "Artist",
        "relationships": {
            "Jill": "friend"
        }
    },
    {
        "name": "John",
        "age": 27,
        "job": "Writer",
        "relationships": {
            "Jill": "partner",
            "Nash": "cousin"
        }
    },
    {
        "name": "Nash",
        "age": 34,
        "job": "Chef",
        "relationships": {
            "John": "cousin",
            "Zalika": "landlord"
        }
    }
]