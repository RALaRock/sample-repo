# ask the person's age
# display the cost of their movie ticket
# < 3 free
# 3 to 12 $10
# > 12 $15

def is_int(val):
    try:
        num = int(val)
    except ValueError:
        return False
    return True

print("Determine the cost of movie tickets based on your age.")
prompt = "Enter the age ('quit' or blank to exit): "
while True:
    answer = input(prompt)
    if is_int(answer):
        age = int(answer)
    elif answer.lower() == 'quit' or answer == '':
        break
    else:
        continue

    if age <= 3:
        print("The ticket will be free.")
    elif age > 12:
        print("The ticket will cost $15.")
    else:
        print("The ticket will cost $10.")

print("\nThank you for using our ticket pricing tool.")