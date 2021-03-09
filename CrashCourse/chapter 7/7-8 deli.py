# make a list of sandwich_orders
# fill it with various sandwiches
# make an empty list of finished_sandwiches
# print a message about making each sandwich
# move the ordered sandwiches to to the finished list
# print a message listing each finished sandwich

sandwich_orders = ["pastrami", "tuna", "italian sausage", "pb&j"]
finished_orders = []
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"We are making your {current_sandwich} sandwich right now.")
    finished_orders.append(current_sandwich)
print("We made the entire order.")
for current_sandwich in finished_orders:
    print(f"\t{current_sandwich}")
