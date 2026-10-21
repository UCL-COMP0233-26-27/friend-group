"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

"""
friendgroup
- friend
   - age
   - profession
   - relationship(dict)
       - otherfriendname
           - relationship
           - connection

"""

my_group = {"Jill": {
                "Age": 26,
                "Profession": "biologist",
                "Relationship": 
                    [{
                        "Name": "Zalika",
                        "Type": "friend"
                    },
                    {
                        "Name": "John",
                        "Type": "partner"
                    }]
                    },
            "Zalika": {
                "Age": 28,
                "Profession": "artist",
                "Relationship": 
                    [{
                        "Name": "Jill",
                        "Type": "friend"
                    },
                    #inferred frmo Nash
                    {
                        "Name": "Nash",
                        "Type": "tenant"
                    }]
                     },
            "John": {
                "Age": 27, 
                "Profession": "writer",
                "Relationship": 
                    [{
                        "Name": "Jill",
                        "Type": "partner"
                    },
                    {
                        "Name": "Nash",
                        "Type": "cousin" #inferred
                    }]
                    },
            "Nash": {
                "Age": 34,
                "Profession": "chef",
                "Relationship": 
                    [{
                        "Name": "John",
                        "Type": "cousin"
                    },
                    {
                        "Name": "Zalika",
                        "Type": "landlord"
                    }]
                    }
}           


# this was a test, does not work properly
"""
def add_person() :
    my_group.update({"Jill": {
                "Age": 26,
                "Profession": "biologist",
                "Relationship": 
                    [{
                        "Name": "Zalika",
                        "Type": "friend"
                    },
                    {
                        "Name": "John",
                        "Type": "partner"
                    }]
                    }
                }
    )
"""

# define a function to add a person, with some default values
def add_person(name="New person", age=20, profession="default", relationship=[]) :
    my_group.update({name: {
                "Age": age,
                "Profession": profession,
                "Relationship": relationship
                        }
                }
    )

#testing adding a person
add_person()
#need to create a list of relations for the new person
relation_list =[{"Name": "John","Type": "teacher"}]
add_person("Diego", 35, "researcher", relation_list)

#trying to add with the relationship inside
add_person("Katie", 36, "postdoc", [{"Name": "Yana","Type": "friend"}])


