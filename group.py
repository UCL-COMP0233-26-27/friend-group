"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

my_group = {
    "Jill": {
        "age": 26,
        "job": "Biologist",
        "relations": [
            {"person": "Zalika", "type": "friend"},
            {"person": "John", "type": "partner"}
        ]
    },

    "Zalika": {
        "age": 28,
        "job": "Artist",
        "relations": [
            {"person": "Jill", "type": "friend"}
        ]
    },

    "John": {
        "age": 27,
        "job": "Writer",
        "relations": [
            {"person": "Jill", "type": "partner"}
        ]
    },

    "Nash": {
        "age": 34,
        "job": "Chef",
        "relations": [
            {"person": "John", "type": "cousin"},
            {"person": "Zalika", "type": "landlord"}
        ]
    }
}

def forget(person1, person2):
    """ removes the connection between two people in the group"""
    if person1 not in my_group or person2 not in my_group:
        print(f"One or both persons not found in the group: {person1}, {person2}")
        return
    my_group[person1]["relations"] = [
        r 
        for r in my_group[person1]["relations"] 
        if r["person"] != person2
    ]
    my_group[person2]["relations"] = [
        r 
        for r in my_group[person2]["relations"] 
        if r["person"] != person1
    ]

def add_relation(name, age, job, relations):
    """ adds a new person with the given characteristics to the group"""
    if name in my_group:
        print(f"{name} already exists in the group.")
        return
    
    my_group[name] = {
        "age": age,
        "job": job,
        "relations": relations
    }

    # add the reverse relations for existing members
    for relation in relations:
        related_person = relation["person"]
        
        if related_person in my_group:
            my_group[related_person]["relations"].append({
                "person": name, 
                "type": relation["type"]
            })
        else:
            print(f"Warning: {related_person} does not exist in the group. Relation not added.")

def average_age():
    """ calculates the average age of the group"""
    if not my_group:
        return 0
    
    total_age = sum(
        person["age"] 
        for person in my_group.values()
    )
    return total_age / len(my_group)

print("Initial group:", my_group)

# Test average_age
print(average_age())

# Test add_relation
add_relation(
    "Alice",
    25,
    "teacher",
    [{"person": "Jill", "type": "friend"}]
)

print(my_group["Alice"])

# Test forget
forget("Alice", "Jill")

print(my_group["Alice"]["relations"])
print(my_group["Jill"]["relations"])