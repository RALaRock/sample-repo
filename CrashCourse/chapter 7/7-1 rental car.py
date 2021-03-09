# ask type of rental car desired
# print "Let me see if I have that car."
cartype = input("What kind of car do you want? ")
print(cartype)
if cartype != '':
    print(f"Hmmmm, let me see is we have a {cartype} available.")
else:
    print("You did not specify a desired car type.")

