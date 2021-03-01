# dictionary is a composite data type like a list
# both are mutable, itemso can be changed
# both are dynamic, can change size
# both can be nested, both can contain other lists or dictionaries
# lists and dictionary differ
# list elements are accessed by their index in the list
# dictionary elements are accessed by their keys
# a dictionary is also called an associative array
# it is a collection of key-value pairs

# defining a dictionary, enclose comma separated list in curly braces
# a semi colon separates each key value pair
# d = {
#     key: value,
#     key: value,
#     key: value, # include the trailing comma to maintain this format
# }

# baseball team locations and names
mlb_teams = {
    "Colorado": "Rockies",
    "Bostom": "Red Sox",
    "Minnesota": "Twins",
    "Los Angeles": "Dodgers",
}
print(type(mlb_teams))
print(mlb_teams)


# adding new key-value pairs
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
print('alient points: ' + str(alien_0['points']))
# adds two key value pairs to dictionary
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)


exit()

# using the dict() function
# d = dict([
#     (key, value),
#     (key, value),
#    (key, value),
# ])
mlb_teams = dict(
    [
        ("Colorado", "Rockies"),
        ("Bostom", "Red Sox"),
        ("Minnesota", "Twins"),
        ("Los Angeles", "Dodgers"),
    ]
)
print(mlb_teams)

# if key values are simple strings can define it like this
mlb_teams = dict(
    Colorado="Rockies",
    Bostom="Red Sox",
    Minnesota="Twins",
    LosAngeles="Dodgers",  # this does not work because of space is Los Angeles
)
print(mlb_teams)

# dictionary elements are NOT accessed by numerical index
# they are accessed by key value by specifying they key in square brackets
print(mlb_teams["LosAngeles"])

# to add an entry to a dictionary specify a new key valye pair
mlb_teams["Kansas City"] = "Royals"
print(mlb_teams)

# to change a value
mlb_teams["Kansas City"] = "Chiefs"
print(mlb_teams)

# to delete an entry
del mlb_teams["Kansas City"]
print(mlb_teams)

# errors if cannpt find the key
# print(mlb_teams[1]) # this raises a can't find key error
# print(mlb_teams['Georgia']) # this raises the same error

# keys can be integers or any other immutable data type
# keys and values do not need to be the same data type
d = {0: "a", 1: "b", 2: "c", "one": 1, "two": 2}
print(d["one"])

