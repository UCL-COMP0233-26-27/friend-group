"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

my_group ={"Jill" : {"age" : 26, 
                     "job":"biologist", 
                     "connections" : [{"name": "Zalika","relationship":"friend" }, 
                                      {"name": "John","relationship":"partner" }]},
            "Zalika" : {"age" : 28,
                    "job":"artist", 
                    "connections" : [{"name": "Jill","relationship":"friend" }]},
            "John" : {"age" : 27,
                    "job":"writer", 
                    "connections" : [{"name": "Jill","relationship":"partner" }]},
            "Nash": {
                    "age": 34,
                    "job": "chef",
                    "connections": [{"name": "John", "relationship": "cousin"},
                                    {"name": "Zalika", "relationship": "landlord"}]}}


# max age of the group
age = [person["age"] for person in my_group.values()]
max(age)
 # average relationship of the group
number_relations =[len(person["connections"]) for person in my_group.values()]
avg_relations = sum(number_relations) /len(number_relations)
print(avg_relations)
#mthe maximum age of people in the group that have at least one relation
age = [person["age"] for person in my_group.values() if len(person["connections"]) > 0]
print(max(age))
#the maximum age of people in the group that have at least one friend
age5 = [person["age"] for person in my_group.values()
  if any(name["relationship"] == "friend" for name in person["connections"])]
print(max(age5))

