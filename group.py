"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

my_group = {
    "Jill": {
        "age": 26,
        "job": "biologist",
        "connections": [
            {"person": "Zalika", "relationship": "friend"},
            {"person": "John", "relationship": "partner"}
        ]
    },

    "Zalika": {
        "age": 28,
        "job": "artist",
        "connections": [
            {"person": "Jill", "relationship": "friend"}
        ]
    },

    "John": {
        "age": 27,
        "job": "writer",
        "connections": [
            {"person": "Jill", "relationship": "partner"},
            {"person": "Nash", "relationship": "cousin"}
        ]
    },

    "Nash": {
        "age": 34,
        "job": "chef",
        "connections": [
            {"person": "John", "relationship": "cousin"},
            {"person": "Zalika", "relationship": "landlord"}
        ]
    }
}
