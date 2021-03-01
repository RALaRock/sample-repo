# create a list and use every function from chapter 3

mountains = []
mountains.append('McKinley')
mountains.append('Adams')
mountains.append('Rainier')
mountains.append('Whitney')
mountains.append('San Gorgonio')
mountains.append('San Jacinto')

print(mountains)
print(mountains[3])
print(mountains[4].lower())
print(mountains[-1])
print(f'The first mountain in the list is {mountains[0]}.')
print(f'The second to last mountain is {mountains[-2]}.')

mountains[0] = 'Tindall'
print(mountains)

mountains.insert(0, 'Mc Kinley')
print(mountains)

del mountains[1]
print(mountains)
# del mountains # deletes entire list
# print(mountains) # fails because list does not exist

removed_mountain = mountains.pop()
print(removed_mountain)
print(mountains)
removed_mountains = mountains.pop(3)
print(removed_mountains)
print(mountains)
mountains.remove('Adams')
print(mountains)

mountains = []
mountains.append('McKinley')
mountains.append('Adams')
mountains.append('Rainier')
mountains.append('Whitney')
mountains.append('San Gorgonio')
mountains.append('San Jacinto')

print(mountains)
print(sorted(mountains))
print(mountains)
mountains.sort()
print(mountains)
mountains.sort(reverse=True)
print(mountains)
mountains.reverse()
print(mountains)
print(len(mountains))
