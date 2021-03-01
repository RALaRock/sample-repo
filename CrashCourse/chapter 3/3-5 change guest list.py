# change guest list of people to invite to dinner

guests = []
guests.append("Roger")
guests.append("Sally")
guests.append("Michael")
guests.append("Robert")

# print an invitation for each guest in guests list
# while len(guests) > 0:
#    print(f"Hi, {guests.pop()}, please join us for dinner.")

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

for i in guests:
    print(f"Hi, {i}, please join us for dinner.")

