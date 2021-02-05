num = 3
print(type(num))
num = 3.14
print(type(num))

print(3 / 2)
# floor division, returns whole number only
print(3 // 2)
# exponents
print(3 ** 2)
# modulus, the remainder after division
print(3 % 2)
# use mod 2 to determine if number even or odd
print(2 % 2)
print(3 % 2)
print(4 % 2)
print(5 % 2)

# incrementing variable
num = 1
print(num)
num = num + 1
num += 1
# can use with other math operators
num *= 10
print(num)

# build in number functions
print(abs(-1))
# rounding
print(round(3.75))
# specify number of digits to round to
print(round(3.75, 1))

# comparison operators, ==, !=, >, <, <=, >=
# returns boolean

# variables that are numbers that look like strings
num_1 = '100'
num_2 = '200'
print(num_1 + num_2)
# to ensure they are numbers use casting
num_1 = int(num_1)
num_2 = int(num_2)
print(num_1 + num_2)
