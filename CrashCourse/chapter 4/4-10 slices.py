# using a list and slicing

# list to work with
values = list(range(10))
print(values)

# print the first three items in the list
print("The first three items in the list are: ")
print(values[:3])
print("Three items from the middle of the list are: ")
slicestart = len(values) // 2 - 1
sliceend = len(values) // 2 + 2
print(values[slicestart:sliceend])
print("The last threeitems in the list are: ")
print(values[-3:])
