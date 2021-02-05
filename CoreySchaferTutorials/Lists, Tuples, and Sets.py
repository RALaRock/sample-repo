# Lists, Tuples, and Sets
# Lists, Tuples allow working with sequential data
# Sets are unordered collecitons of values with no duplicates

# lists
courses = ["history", "math", "physics", "compsci"]
print(courses)
print(len(courses))  # number of elemensts in list
print(courses[0])
print(courses[1])
print(courses[2])
print(courses[3])
print(courses[len(courses) - 1])
# negative indexes start from end of the list and work toward beginning
print(courses[-1])  # -1 is last item in list
# can extract a range of values
print(courses[0:2])  # first two elements
print(courses[:2])  # first element implied
print(courses[-1])  # using negative starts from end of list
print(courses[2:])  # gets the first two elements of the list
# if the result is a single element, it is not a list
# if the result is more than one element, it is s list
# these are all forms of a technique called 'slicing'

# list methods
# add an item to end of list
courses.append('art')
print(courses)
