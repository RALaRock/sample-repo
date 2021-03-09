# some useful functions

# function strips leading, training and extra spaces in a string
# returns the space stripped string
def strip_all_spaces(string):
    return " ".join(string.split())


# end def

# replace an item in a list with another item
# needs error checking for empty list and olditem not existing
# EX: print(list_replace(guests, noshow, replacement))
def list_replace(items, olditem, newitem):
    items[items.index(olditem)] = newitem
    return items


# end def

# test if a string value can be converted into a float
def is_float(val):
    try:
        num = float(val)
    except ValueError:
        return False
    return True


# test if a string value can be converted into an integer
def is_int(val):
    try:
        num = int(val)
    except ValueError:
        return False
    return True
