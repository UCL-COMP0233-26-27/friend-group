"""An example of how to represent a group of acquaintances in Python."""

# Import module(s)
import sys

# We have the following information for each person, with categories being
# "name", "age", "job", and "relationship":
#   * Jill is 26, a biologist, and she is Zalika's friend and John's partner.
#   * Zalika is 28, an artist, and Jill's friend.
#   * John is 27, a writer, and Jill's partner.
#   * Nash is 34, a chef, John's cousin and Zalika's landlord.
#
# We need to create a structure to define this group of people, which we
# will call `my_group`.

# Create one dictionary for each friend.
# This directory has keys "name", "age", "job", and "relation".
# For "relation", we use a placeholder value with `None`, which will be 
# replaced later with the correct information we will create in a string.
friend1 = {"name": "Jill", "age": 26, "job": "biologist", "relation": None}
friend2 = {"name": "Zalika", "age": 28, "job": "artist", "relation": None}
friend3 = {"name": "John", "age": 27, "job": "writer", "relation": None}
friend4 = {"name": "Nash", "age": 34, "job": "chef", "relation": None}

# Create relationships for each friend.
# We create a pre-defined string with each person's relationship(s) to
# other friend(s).
friend1_rel = f'{friend2["name"]}\'s friend and {friend3["name"]}\'s partner'
friend2_rel = f'{friend1["name"]}\'s friend'
friend3_rel = f'{friend1["name"]}\'s partner'
friend4_rel = f'{friend3["name"]}\'s cousin and {friend2["name"]}\'s landlord'

# Put each friend in a dictionary called `my_group`
# Could have been done using a list, but a dictionary allows to give
# a specific name to each entry
my_group = {"Jill":friend1, "Zalika": friend2, "John": friend3, "Nash":friend4}

# Example: check that the dictionary `my_group` works as intended
# and that we have not assigned the wrong name to a dictionary!
# If that happens, let us know so that we can fix the code above
count = 0
for name in ["Jill", "Zalika", "John", "Nash"]:
    count =+ 1
    if( my_group[name]["name"] != name ):
        message = ( f'You have assigned the wrong key ({name}) to element in '
                   f'position {count} ({my_group[name]["name"]}\'s dictionary) '
                   f'in dictionary \"my_group\"' )
        sys.exit( message )

# Replace `None` in key "relation" with the correct relationship for each friend
my_group["Jill"]["relation"] = friend1_rel
my_group["Zalika"]["relation"] = friend2_rel
my_group["John"]["relation"] = friend3_rel
my_group["Nash"]["relation"] = friend4_rel

# Print information about each friend's relationship(s)
print( "\n[[ Friend's relationships ]]\n")
print("Jill's relationship(s):", my_group["Jill"]["relation"])
print("Zalika's relationship(s):", my_group["Zalika"]["relation"])
print("John's relationship(s):", my_group["John"]["relation"])
print("Nash's relationship(s):", my_group["Nash"]["relation"])
