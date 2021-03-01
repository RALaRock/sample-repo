# exploring the scope of variables
# dir() returns the names in the current scope

print("before a_num created, scope")
print(dir())

a_num = 10
print("after a_num created, scope")
print(dir())
# ['__builtins__' .... '__spec__', 'a_num']


def some_func():
    print("inside some_func scope")
    b_num = 11
    print(dir())


some_func()
# ['b_num']

print("after some_func, scope")
print(dir())
# ['__builtins__' ... '__spec__', 'a_num', 'some_func']


def outer_func():
    c_num = 12

    def inner_func():
        d_num = 13
        print(dir(), " - names in inner_func")

    e_num = 14
    inner_func()
    print(dir(), " - names in outer_func")


outer_func()
# ['d_num']  - names in inner_func
# ['c_num', 'e_num', 'inner_func']  - names in outer_func


# Unless explicitly specified by using global,
# reassigning a global name inside a local namespace
# creates a new local variable with the same name.
# This is evident from the following code.
a_num = 10
print("a_num = " + a_num)  # a_num not global yet
b_num = 11


def outer_func():
    global a_num
    a_num = 15
    b_num = 16

    def inner_func():
        global a_num  # global changes scope to
        # everywhere from this point on
        a_num = 20
        b_num = 21
        print("a_num inside inner_func :", a_num)
        print("b_num inside inner_func :", b_num)

    inner_func()
    print("a_num inside outer_func :", a_num)
    print("b_num inside outer_func :", b_num)


outer_func()
print("a_num outside all functions :", a_num)
print("b_num outside all functions :", b_num)

# a_num inside inner_func : 20
# b_num inside inner_func : 21

# a_num inside outer_func : 20
# b_num inside outer_func : 16

# a_num outside all functions : 20
# b_num outside all functions : 11