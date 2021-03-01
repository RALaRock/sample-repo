# ad an if test to make suer the list of users is not empty
# if the list is empty print
# "We need to find some users."
# test this my removing the list items

usernames = [
    "Jaden",
    "robert",
    "cinDy",
    "SAMUEL",
    "admin",
    "frank",  # note trailing comma required here to maintain list structure
]

if usernames:
    for username in usernames:
        if username.lower() == "admin":
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {username.title()}, thank you for logging in again.")
else:
    print("We need to find some users.")

# test this my removing the list items
usernames = []
if usernames:
    for username in usernames:
        if username.lower() == "admin":
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {username.title()}, thank you for logging in again.")
else:
    print("We need to find some users.")
