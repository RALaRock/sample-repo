# use a dictionary to store favorite numbers for 5 people

favorite_numbers = {
    'paul': 25,
    'sam': 12,
    'bill': 43,
    'kris': 56,
    'david': 90,
}

# for each key in favorite_numbers
for key in favorite_numbers:
    # print the associated value
    thiskey = key.title()
    keyvalue = favorite_numbers.get(key)
    # note using f string automatically converts integer value to string
    print(f"{thiskey}'s favorite number is {keyvalue}")
