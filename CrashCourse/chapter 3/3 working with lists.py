# a list of names
names = ["beate", "robert", "david"]
print(names)

# accessing the elements of a list
# list indexes are based at 0
print(names[0])

# a -1 index returns the last item in the list
print(names[-1])
# -2 returns the second item from the end, -2 the third, etc.

# can use items from a list like any other variable
print(f"The last name in the list is: {names[-1].title()}")
