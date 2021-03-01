# store numbers 1 to 9 in a list
# print the proper ordinal for each number

numbers = range(1, 10)

for number in numbers:
    if number == 1:
        subscript = "st"
    elif number == 2:
        subscript = "nd"
    elif number == 3:
        subscript = "rd"
    else:
        subscript = "th"
    print(str(number) + subscript)
