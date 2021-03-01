# make a list of at least 5 users called current_users
# make another list of five users called new_users
# make sure one or two new_users are in the current_users
# check to see if a user name has been used and if so print
# "{username} has already been used. Enter a different user name"

current_users = [
    "Jaden",
    "robert",
    "cinDy",
    "SAMUEL",
    "frank",  # note trailing comma required here to maintain list structure
]

new_users = [
    "Cindy",
    "Samuel",
    "August",
    "RALPH",
]

# convert the lists to lower case for doing comparison
newusers = [x.lower() for x in new_users]
currentusers = [x.lower() for x in current_users]

for username in newusers:
    if username in currentusers:
        # print the name as stored in the current user name list
        print(f"{current_users[currentusers.index(username)]} has already been used. Try a different user name.")
    else:
        print(f"Welcome {username.title()}!")
