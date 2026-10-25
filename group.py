"""An example of how to represent a group of acquaintances in Python."""

# data structure

"""
friendgroup {dict}
- friend {dict}
   - age
   - profession
   - relationship [list]
        - {dict}
            - relationship name
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
                    #inferred from Nash
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


#
# new section on comprehensions
"""
Task requirement
comprehension expressions to your group.py file so that it prints out the following when the script is run:
 1   the maximum age of people in the group
 2   the average (mean) number of relations among members of the group
 3   the maximum age of people in the group that have at least one relation
 4   [more advanced] the maximum age of people in the group that have at least one friend
"""
##############
# summary
##############
# task 1 -  the maximum age of people in the group
print(max([my_group[person]["Age"] for person in my_group]))

# task  2   the average (mean) number of relations among members of the group
# need a mean average command
from numpy import mean
print(mean(len(my_group[person]["Relationship"])))

# task  3 the maximum age of people in the group that have at least one relation
print(max([my_group[person]["Age"] for person in my_group if len(my_group[person]["Relationship"]) > 0]))
# note, all at two relationships so couldn't really test this

# task 4  [more advanced] the maximum age of people in the group that have at least one friend
print(max([my_group[person]["Age"] 
           for person in my_group 
           for relation in my_group[person]["Relationship"]
           if relation['Type'] == "friend"]))


########
# task 1 -  the maximum age of people in the group
######### 
# testing extracting info
# Person
my_group["Jill"]
# age
my_group["Jill"]["Age"]
# code, extracting with for loop
age_list = [] # create list of ages
print(age_list)        
for person in my_group:
    print (person)
    print (my_group[person])
    print (my_group[person]["Age"])
    age_list.append (my_group[person]["Age"])
print(age_list)
print(max(age_list))
max(age_list)
#age_list2 = []
#age_list2 = [my_group[person]["Age"] for person in my_group]

#as comprehension
#age_list2.append(my_group[person]["Age"] for person in my_group) 
#age_list2.append(age for person in my_group: age = my_group[person]["Age"]) 
print(max([my_group[person]["Age"] for person in my_group]))

########
# task  2   the average (mean) number of relations among members of the group
######### 
# code, extracting with for loop
for person in my_group:
#    print (person)
#    print (my_group[person])
    print (my_group[person]["Relationship"])
    print (len(my_group[person]["Relationship"]))

# as comprehension
# need a mean average command
from numpy import mean
print(mean(len(my_group[person]["Relationship"])))


####################
# task  3 the maximum age of people in the group 
# that have at least one relation
#################### 
# code, extracting with for loop
print(age_list)
for person in my_group:
#    print (person)
#    print (my_group[person])
    print (my_group[person]["Relationship"])
    print (len(my_group[person]["Relationship"]))
    #check friend number
    if len(my_group[person]["Relationship"]) > 1:
       age_list.append (my_group[person]["Age"])
    print(age_list)

# as comprehension
# check full list
# [my_group[person]["Age"] for person in my_group if len(my_group[person]["Relationship"]) > 0]
print(max([my_group[person]["Age"] for person in my_group if len(my_group[person]["Relationship"]) > 0]))
#print(max([my_group[person]["Age"] for person in my_group if len(my_group[person]["Relationship"]) > 1]))


####################
# task 4  [more advanced] the maximum age of 
# people in the group that have at least one friend
###################
age_list = []
print(age_list)
people_with_friends = []
for person in my_group:
#    print (person)
#    print (my_group[person])
#    print (my_group[person]["Relationship"])
#    print (my_group[person]["Relationship"][0])
    for relation in my_group[person]["Relationship"]:
#        print(relation['Type'])
        if relation['Type'] == "friend":
            print(person, "aged", my_group[person]["Age"], "has a friend")
            age_list.append (my_group[person]["Age"])
    print(age_list)

print(max(age_list))
# as comprehension
print(max([my_group[person]["Age"] 
           for person in my_group 
           for relation in my_group[person]["Relationship"]
           if relation['Type'] == "friend"]))





# writing a json file
import json

# writing to file
with open('friend-group.json', 'w') as filename:
    json.dump(my_group, filename, indent=4, sort_keys=True)
# loading from file
with open('friend-group.json', 'r') as file:
     loaded_friend_group = json.load(file)
print(loaded_friend_group)

