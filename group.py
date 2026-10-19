"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

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

for key in my_group:
    print(f"{key} is a {my_group[key]['job']} and is {my_group[key]['age']} years old.")
    for connection in my_group[key]["connections"]:
        print(f"  - {connection['name']}'s {connection['relationship']}")