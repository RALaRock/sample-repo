# branching based on a condition
#
# IF condition:
#   statements
# elif:
#   statements
# else:
#   statements
#
# condition is something that evalueates to True or False

# 0 = false
# any other number, positive or negative = true
if 0:
    print("true")
else:
    print("false")

# conditional tests for equivalents are case sensitive
# test != Test
test = "Value"
test2 = "value"
# use method to make both strings the same case for comparison
if test.lower() == test2.lower():
    print("same")
else:
    print("different")

# conditional operators
# == equal
# != not equal
# < less than
# <=
# > greater than
# >=
# and, both true
# or, either or both true
# in, true if value in a list
# not in, true if value not in a list

# ternary conditionals
# expression1 if conditional else expression2
weather = "good"
print("let's fly") if weather == "good" else print("let's watch tv")
# find the greater of two numbers
a = 5
b = 10
print("a is greater") if a > 5 else print("b is greater")
# can be grouped together in a kind of switch operation
x = 3
s = (
    "foo"
    if (x == 1)
    else "bar"
    if (x == 2)
    else "baz"
    if (x == 3)
    else "qux"
    if (x == 4)
    else "quux"
)
print(s)

# pass operator is used to define an empty code block
# useful as a placeholder for code to add later
if test:
    pass
morecodehere = ""

# using if and lists
requested_toppings = ["mushrooms", "green peppers", "extra cheese"]
if "green peppers" in requested_toppings:
    print(f"sorry we are out of green peppers")
    requested_toppings.remove("green peppers")
print(f"your pizza will come with {' and '.join(requested_toppings)}")

# check if list has any items before processing
toppings = []
if toppings:  # returns true if the list has at least one item
    # do stuff to list
    toppings
else:
    # do something about empty list
    toppings.append("crud")

print()

# using two lists
available_toppings = [
    "mushrooms",
    "green peppers",
    "extra cheese",
    "mozza",
    "sauce",
    "pepperoni",
]
requested_toppings = ["mushrooms", "cat poo", "extra cheese"]
requested_topping = ""
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        toppings.append(requested_topping)
    else:
        print(f"{requested_topping} is not available")

print(f"Your toppings will be - {' '.join(toppings)}")
print()

# if statement styling guide
# best to use single spacing around operators
# if x>y: is not as good as if x > x:
