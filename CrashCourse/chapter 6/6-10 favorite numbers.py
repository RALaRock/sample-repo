# modify 6-2 so each person has more than one favorite number
# print each person's numbers

# use a dictionary to store favorite numbers for 5 people

favorite_numbers = {
    "paul": [30],
    "sam": [],
    "bill": [255, 102, 425, 370],
    "kris": [6, 122, 415, 370],
    "david": [285, 129, 445, 310],
}

# for each key in favorite_numbers
for name in favorite_numbers:
    # print the associated value
    thisname = name.title()
    numbers = favorite_numbers.get(name)
    # note using f string automatically converts integer value to string
    if len(numbers) == 1:
        print(f"{thisname}'s favorite number is {numbers[0]}.")
    elif len(numbers) > 1:
        # convert the integer number list to a comma separated string
        numberstring = ", ".join([str(i) for i in numbers])
        print(f"{thisname}'s favorite numbers are: " + numberstring + ".")
    else:
        print(f"{thisname} has no favorite numbers.")
print()
