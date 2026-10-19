"""An example of how to represent a group of acquaintances in Python."""

# Jill is 26, a biologist and she is Zalika's friend and John's partner.
# Zalika is 28, an artist, and Jill's friend
# John is 27, a writer, and Jill's partner.
# Nash is 34, a chef, John's cousin and Zalika's landlord.

# Your code to go here...
import numpy as np


# Each row contains a name and that person's details.
my_group = {
    "Jill": [[26, "biologist", ["Zalika", "John"]]],
    "Zalika": [[28, "artist", ["Jill"]]],
    "John": [[27, "writer", ["Jill"]]],
    "Nash": [[34, "chef", ["John", "Zalika"]]],
}

# Keep the nested lists as objects in a two-dimensional array.
print(my_group["Jill"])
