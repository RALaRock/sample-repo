# ask the user for a number
# report whether or not the number is evenly divisible by 10
number = input("Enter a number: ")
if int(number) % 10 == 0:
    print(f"{number} is evenly divisible by 10.")