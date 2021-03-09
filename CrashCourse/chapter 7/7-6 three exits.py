# use a conditional test  in the while loop to exit
# use a counting varible to exit
# use a break statement to exit

# test if a string can be converted to an integer
def is_int(val):
    try:
        num = int(val)
    except ValueError:
        return False
    return True


print("Determine the cost of movie tickets based on your age.")
prompt = "Enter the age ('quit' or blank to exit): "
loop_count = 0
loop_max = 5
while True:
    # ask for age and process quit conditions
    answer = input(prompt)
    # limit the number of times this can be run
    loop_count += 1
    if loop_count >= loop_max:  # limit number of tries
        print("Max number of ticket prices checked.")
        break
    elif is_int(answer):  # if answer is legit make it integer
        age = int(answer)
    elif answer.lower() == "quit" or answer == "":  # look for quit condition
        print("All done.")
        break
    else:
        print("I don't know what to do with that answer, please try again.")
        continue

    # show the ticket cost based on age
    if age <= 3:
        print("The ticket will be free.")
    elif age > 12:
        print("The ticket will cost $15.")
    else:
        print("The ticket will cost $10.")

print("\nThank you for using our ticket pricing tool.")
