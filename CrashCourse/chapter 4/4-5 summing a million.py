# make a list of numbers from 1 to 1 million
# use min() max() to verify numbers range
# use sum() to total the numbers and print the sum

values = []
for value in range(1, 1000001):
    values.append(value)
print(min(values))
print(max(values))
print(sum(values))
