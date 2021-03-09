# get all the desired pizza toppings from a user
# print a list of toppings for their pizza
toppings = []
prompt = "Enter the name of a desired topping for your pizza: "
while True:
    topping = input(prompt)
    if topping == '':  # blank answer, exit
        break
    elif topping.lower() == 'quit':
        break
    else:
        # build a list of toppings
        toppings.append(topping)
for topping in toppings:
    print(topping)
