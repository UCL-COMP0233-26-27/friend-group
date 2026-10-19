"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...


Jill = {"name": "Jill", "age": 26, 
           "Jobs": "Biologist", "Connections":[Zalika, John] }

Zalika = {"name": "Zalika", "age":28,
            "Jobs":"Artist", "Connections":[Jill, Nash] }

John = {"name": "John", "age": 27,
            "Jobs":"Writer", "Connections":[Jill, Nash]}

Nash = {"name": "Nash", "age": 34,
            "Jobs": ["Chef", "Landlord"], "Connections":[Zalika, John]}


print(Nash["age"])
Jill.keys()
John.values()

## Jill is 26, a biologist and she is Zalika's friend and John's partner.
## Zalika is 28, an artist, and Jill's friend
## John is 27, a writer, and Jill's partner.
## Nash is 34, a chef, John's cousin and Zalika's landlord.