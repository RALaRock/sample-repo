# make a dictionary of 3 major rivers and the countries they pass through

rivers = {"nile": "egypt", "mississippi": "united states", "yukon": "canada"}

# loop and print each river and where it runs
for river, country in rivers.items():
    print(f"{river.title()} runs through {country.title()}")

# print the name of each river only
print()
for river in rivers:
    print(river.title())
# this does the same thing
print()
for river in rivers.keys():
    print(river.title())

# print the name of each country only
print()
for country in rivers.values():
    print(country.title())

print()