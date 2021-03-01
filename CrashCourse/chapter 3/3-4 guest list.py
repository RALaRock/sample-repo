# invite list of people to dinner

guests = []
guests.append("Roger")
guests.append("Sally")
guests.append("Michael")
guests.append("Robert")

# print an invitation for each guest in guests list
while len(guests) > 0:
    print(f"Hi, {guests.pop()}, please join us for dinner.")
