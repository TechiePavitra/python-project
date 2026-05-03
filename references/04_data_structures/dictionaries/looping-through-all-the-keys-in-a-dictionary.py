members = {
    # name and age
    "john": 23,
    "ram": 41,
    "janice": 72,
    "michael": 35,
    "umesh": 15,
}

# Cleaner Beginner Way
# Easy to understand and clear
for name in members.keys():
    print(name.title())

# Profesional Way
# as the .keys() is an default behaviour don't use .keys() / omit .keys()
# More Pythonic Code
for name in members:
    print(name.title())