message = "Hello World"
# use double quotes on any string that contains single quotes
message = "Robert's World"
# use single quotes to contain string that contains double quotes
message = '"Hello World"'
# use escape character "\" before quote
message = "Robert's World"
# use three double quotes to create string with multiple lines
message = """This is the first line.
This is the second line.
This is the third line."""
print(message)

# working with strings
length = len(message)
print(length)
# strings can be used with an index like an array
print(message[10])
# indexes start at 0
# index error as index is past end of string
# print(message[110])
# can index a range by adding the number of characters to extract
print(message[0:6])
# can leave off start point and it will assume the 0 beginning
print(message[:6])
# can also leave off the range to get until the end of the string
print(message[6:])
# this is called string slicing

# data types
# string methods
message = "Hello World"
print(message.lower)
print(message.upper)
print(message.count("Hello"))
print(message.count("l"))
print(message.find("World"))
# returns -1 if the string is not found
print(message.replace("Hello", "Goodbye"))

# concatenate strings
greeting = "Hello"
name = "Michael"
message = greeting + ", " + name + ". Welcome!"
print(message)
# using formatted string, {} are placeholders for strings to insert
message = "{}, {}. Welcome!".format(greeting, name)
print(message)
# python 3.6+ have f strings, add f to start of string
# then pass variables directly within the placeholders
message = f"{greeting}, {name}. Welcome!"
print(message)
# can put code in the placeholder
message = f"{greeting}, {name.upper()}. Welcome!"
print(message)

# dir function shows all attributes and methods of a given variable
print(dir(name))
# can use help function run on the class, str is the string class
# print(help(str))
print(help(str.lower))
