# python always loop through the order you inserted in dictionary.
# like in this distionary the ordering the name.

database = {
# name (keys) cities (values)
    "mohit": "surat",
    "sumit": "rajkot",
    "rajesh": "mehsana",
    "ram": "valsad",
    "aditi": "mumbai",
    "mangesh": "ahmedabad",
    "dharmik": "bhavnagar",
}

# for name
for name in sorted(database.keys()):
    print(name.title())

# blank space
print()

# for cities 
for city in sorted(database.values()):
    print(city.title())
    
# always use .items() when you need to use key and value at same time.
# like this one 
Test = True
for name, city in sorted(database.items()):
    if Test:
        print(name.title())
    else:
        print(city.title())
        
# note that .sort() method only applies for the lists, while .sorted applies for any iterable (repeated things)

