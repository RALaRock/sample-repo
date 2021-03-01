# print a greeting to each name, same greeting for each
motorcycles = ["Honda", "Yamaha", "KTM", "Suzuki"]

# i is assigned a value from names for each iteration
for i in motorcycles:
    if i == "Honda" or i == "Yamaha":
        print(f'I have raced on a {i}.')
    else:
        print(f'I have not raced on a {i}.')
