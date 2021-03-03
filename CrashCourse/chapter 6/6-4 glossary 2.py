# create a glossary of five programming words and definitions
# print the word and definition separated with a colon

glossary = {
    "loop": "a repeating structure",
    "list": "a collection if items",
    "argument": "a value passed in a function",
    "method": "an assembly of statments packed into a routine",
    "language": "the syntax for a set of program instructions",
    "key": "a pointer to a value in a dictionary",
    "value": "the informatikon referred to by a key in a dictionary",
    "file": "a container for program code and other stuff",
    "interpreter": "a program that converts code into machine code on the fly",
    "compiler": "a program that converts code into machine code"
}

for keyname in glossary:
    value = glossary[keyname].title()
    print(f"{keyname.title()}:")
    print(f"    {value}.")
