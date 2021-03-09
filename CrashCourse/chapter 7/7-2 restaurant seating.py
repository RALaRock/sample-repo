# ask how many people in you party
# if answer is > 8 then print you'll have to wait message
guests = input("How many people are in your party?")
if int(guests) > 8:
    print("You'll have to wait for a table.")
else:
    print(f"We can seat your party of {guests} right away.")