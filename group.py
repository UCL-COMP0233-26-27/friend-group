"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

my_group = {
    "Jill":{
        "age": 26,
        "occupation": "biologist",
        "relationships":{
            "friend": "Zalika",
            "partner": "John"
        }
    },

    "Zalika":{
        "age": 28,
        "occupation": "artist",
        "ralationships":{
            "friend": "Jill",
            "landlord": "Nash"
        }
    },

    "John":{
        "age": 27,
        "occupation": "writer",
        "relationships":{
            "partner": "Jill",
            "cousin": "Nash"
        }
    },

    "Nash":{
        "age": 34,
        "occupation": "chef",
        "relationships":{
            "cousin": "John",
            "tenant": "Zalika"
        }
    }
}


print(my_group["Jill"])
print(my_group["Jill"]["relationships"]["friend"])  # Output: Zalika