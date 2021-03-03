# make a pet dictionaries that include:
# kind of animal, owner's name
# store them in a pets list
# loop through list and print everything about each pet

# list of pets containing dictionaries for each pet
pets = [
    {"species": "dog", "owner": "sam"},
    {"species": "cat", "owner": "bill"},
    {"species": "mouse", "owner": "kim"},
    {"species": "rat", "owner": "bernie"},
]
print()
print(type(pets))
print(pets)
print(type(pets[0]))
print(pets[0])
print()
# print out everything about each pet
for pet in pets:
    print(f"Owner: {pet['owner'].title()}")
    print(f"Type of pet: {pet['species']}")
    print()
