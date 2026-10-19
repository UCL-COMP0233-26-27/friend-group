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

print(my_group)

