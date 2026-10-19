my_group = {
    "Jill": {
        "age": 26,
        "job": "biologist",
        "connections": [
            {"name": "Zalika", "relationship": "friend"},
            {"name": "John", "relationship": "partner"}
        ]
    },
    "Zalika": {
        "age": 28,
        "job": "artist",
        "connections": [
            {"name": "Jill", "relationship": "friend"}
        ]
    },
    "John": {
        "age": 27,
        "job": "writer",
        "connections": [
            {"name": "Jill", "relationship": "partner"}
        ]
    },
    "Nash": {
        "age": 34,
        "job": "chef",
        "connections": [
            {"name": "John", "relationship": "cousin"},
            {"name": "Zalika", "relationship": "landlord"}
        ]
    }
}

print(my_group)
