"""An example of how to represent a group of acquaintances in Python."""

# Create an example instance, in an editor or a notebook, of a structure for this group:

# Jill is 26, a biologist and she is Zalika's friend and John's partner.
# Zalika is 28, an artist, and Jill's friend
# John is 27, a writer, and Jill's partner.
# Nash is 34, a chef, John's cousin and Zalika's landlord.

# Create one dictionary for each friend
friend1 = {"name": "Jill", "age": 26, "job": "biologist", "relation": None}
friend2 = {"name": "Zalika", "age": 28, "job": "artist", "relation": None}
friend3 = {"name": "John", "age": 27, "job": "writer", "relation": None}
friend4 = {"name": "Nash", "age": 34, "job": "chef", "relation": None}

# Create relationships for each friend
friend1_rel = print(friend2["name"], "'s friend and", friend3["name"], "'s partner")
friend2_rel = print(friend1["name"], "'s friend")
friend3_rel = print(friend1["name"], "'s partner")
friend4_rel = print(friend3["name"], "'s cousin and", friend2["name"], "'s lanrdlord")

# Put each friend in a group
my_group = [friend1, friend2, friend3, friend4]

# TO DO: Replace `None` with the correct relationship
