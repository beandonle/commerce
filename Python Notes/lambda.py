people = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Draco", "house": "Slytherin"}
]

"""
def f(person):
    return person["house"]

# sort function needs defintion on how to sort the dict
people.sort(key=f)

"""

# same as above but uses lambda instead of calling a function
people.sort(key=lambda people : people["name"])

print(people)