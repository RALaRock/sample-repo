
name = "   Robert   LaRock    "

# function strips leading, training and extra spaces in a string
# returns the space stripped string
def strip_all_spaces(string):
    return(" ".join(string.split()))
# end func

print(strip_all_spaces(name))
