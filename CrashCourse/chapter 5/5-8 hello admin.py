# make a list of 5 or more user names
# including the name admin
# print a greeting to each user after they log into a site
# if the user name is admin print a special greeting
# "Hello admin, would you like to see a status report?"
# otherwise print
# "Hello [username], thank you for logging in again."

usernames = [
    "Jaden",
    "robert",
    "cinDy",
    "SAMUEL",
    "admin",
    "frank",  # note trailing comma required here to maintain list structure
]

for username in usernames:
    if username.lower() == "admin":
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {username.title()}, thank you for logging in again.")
