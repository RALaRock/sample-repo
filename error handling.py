# learning to handle exception errors
# https://www.datacamp.com/community/tutorials/exception-handling-python

list = [1, 2, 3, 4]
print(list)
itemtoremove = input("enter the item number to remove")
print(itemtoremove)

try:
    # inp = input()
    # print('Press Ctrl-C or interrupt the Kernel.')
    list.remove(int(itemtoremove))

except ValueError:
    # do not use bare except, include the type of exception to
    # be handled or Exception if all exceptions to be handled
    # print('Caught keyboard interrupt.')
    print("that item number is not in the list")

else:
    # print('No exception occurred.')
    print(list)
