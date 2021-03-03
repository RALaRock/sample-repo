# create a dictionary to store info about a person
#   first name, last name, age, city where they live

person = {}

person = {
    "first_name": "sally",
    "last_name": "smith",
    "age": 25,
    "city": "Los Angeles",
}

print(person["first_name"])
# this fails if the key does not exist, for example
# print(person['bad_keyname']) causes a Traceback error
# use get() to deal with keys that may not exist
print(person.get("first_name"))
# example of key that does not exist
keyname = "name"
print(person.get("name"))  # get() returns None if key does not exist
if person.get("name") == None:
    print(person.get(keyname, f"{keyname.upper()} does not exist."))
print()
