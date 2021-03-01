# playing with lists of things you would like to see

locations = []
locations.append("Machu Pichu")
locations.append("Bogota")
locations.append("Palau")
locations.append("Brisbane")
locations.append("Skagway")
locations.append("Moscow")

# list in original order
print(locations)

# locations is sorted order
print(sorted(locations))
print(locations)

# locations sorted in reverse without permanently changing order
print(sorted(locations, reverse=True))
print(locations)

# permantently reverse list
locations.reverse()
print(locations)

# reverse again
locations.reverse()
print(locations)

# permanently sort locations
locations.sort()
print(locations)
