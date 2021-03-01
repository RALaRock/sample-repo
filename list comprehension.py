# list comprehension is a shorter symtax to create a new
# list based on the values of an exising list

# longer way
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newfruits = []
for fruit in fruits:
    if 'a' in fruit:
        newfruits.append(fruit)
print(newfruits)

# using list comprehension
newfruits = [x for x in fruits if 'a' in x]
print(newfruits)

# create a new list from an existing one
newfruits = [fruit for fruit in fruits]

# syntax
# newlist = [expression FOR item IN iterable IF condition == True]
# iterable can be any object, like a list
# can use range() to create an iterable object
# expression can be anything that modifies the current iterable
# the IF portion is optiona;
newfruits = [x.upper() for x in fruits if 'a' in x]
print(newfruits)

# this creates a class object of numbers
snumbers = range(10)
print(type(snumbers))

# this creates a list object of numbers
numbers = [x for x in range(100)]
print(type(numbers))
print(numbers)

# get the values divisible by 3 and double the result
newnumbers = [x * 2 for x in numbers if x % 3 == 0]
print(newnumbers)

# more fruity goodness with comprehensions
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# if x is banana return orange otherwise return the fruit
newfruits = [x if x != 'banana' else 'orange' for x in fruits]
# this is how to iterate through a list modifying all list
# for output
print([fruit.title() for fruit in fruits])
