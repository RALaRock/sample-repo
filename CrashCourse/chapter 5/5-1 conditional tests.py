# create at least 5 false and 5 true tests
# and predict the outcome of each

cars = "bmw", "ford", "chevy", "merc"
if "bmw" in cars:
    print("bmw in cars")
if cars[0] == "ford":
    print("the first car is a ford")
elif cars[1] == "ford":
    print("the second car is a ford")
else:
    print("weird, it should be the second car")

if "chevy" in cars:
    print("chevy is in the club")

# using a ternary conditional
print("chevy") if ("chevy" in cars) else print("chevy missing")
