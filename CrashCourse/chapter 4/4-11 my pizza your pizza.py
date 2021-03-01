# playing with pizzas

# working with for loops and pizzas

pizzas = ["pepperoni", "sausage", "cheese", "mushroom", "three cheese"]

# print out pizza
print("Pizzas:")
for pizza in pizzas:
    print(pizza)
print()

# make a copy of the pizzas
friend_pizzas = pizzas[:]

# add a new pizza to the original list
pizzas.append("hawaiian")
# add a different pizza to friend pizzas
friend_pizzas.append("margarita")

# prove lists are different
print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)
print()
print("My friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)
print()
