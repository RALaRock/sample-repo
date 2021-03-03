# create a dictionary to store info about a person
#   first name, last name, age, city where they live

people = {
    "ssmith": {
        "first_name": "sally",
        "last_name": "smith",
        "age": 25,
        "city": "los angeles",
    },
    "rjones": {
        "first_name": "roger",
        "last_name": "jones",
        "age": 30,
        "city": "dallas",
    },
    "kcreedon": {
        "first_name": "kathy",
        "last_name": "creedon",
        "age": 48,
        "city": "pasadena",
    },
}
print(people)
print()

# using get() in case key does not exist
person = people.get("ssmith")
print(person)
print()

for username, userinfo in people.items():
    print(f"\nUsername: {username}")
    fullname = f"{userinfo.get('first_name')} {userinfo.get('last_name')}"
    print(f"\tName: {fullname.title()}")
    print(f"\tAge: {userinfo.get('age')}")
    print(f"\tLocation: {userinfo.get('city').title()}")
