# change guest list of people to invite to dinner

guests = []
guests.append("Roger")
guests.append("Sally")
guests.append("Michael")
guests.append("Robert")

# print an invitation for each guest in guests list
# while len(guests) > 0:
#    print(f"Hi, {guests.pop()}, please join us for dinner.")

# print invitations
for i in guests:
    print(f"Hi, {i}, please join us for dinner.")

print()
noshow = "Sally"
print(f"Unfortuately, {noshow}, cannot make it.")
replacement = "Janice"
print(f"I will invite {replacement} instead.")
print()

# replace no show guest with replacement
guests[guests.index(noshow)] = replacement

# print invitations
for i in guests:
    print(f"Hi, {i}, please join us for dinner.")

print()
print("I found a bigger table. So, I am going to invite a few more guests.")

newguests = []
newguests.append("Clementine")
newguests.append("Joshua")
newguests.append("Franklin")
# this also works
# newguests = ['test 1', 'test 2', 'test 3']

# insert new guest at start of invite list
guests.insert(0, newguests[0])
# insert new guest in middle of list
middle_of_guests = int(len(guests) / 2) + 1
guests.insert(middle_of_guests, newguests[1])
# add new guest to end of the list
guests.append(newguests[2])

# print invitations
for i in guests:
    print(f"Hi, {i}, please join us for dinner.")

print()

# reduce guest list to two people
print("Unfortunately, our table will not be ready in time.")
print("I will only be able to invite two people.")

while len(guests) > 2:
    uninvited = guests.pop()
    print(f"Unfortunately, {uninvited} we must cancel our invitation.")

# print invitations
for i in guests:
    print(f"Hi, {i}, please join us for dinner.")

print()

# delete the last two list items using del()
del guests[0]
del guests[0]  # same index because list now only one element long
print(guests)

