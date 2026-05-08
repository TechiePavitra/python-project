# Make a dictionary containing three major rivers and the country each river runs through. One key-value pair might be 'nile': 'egypt'.
# Use a loop to print a sentence about each river, such as The Nile runs through Egypt.
# Use a loop to print the name of each river included in the dictionary.
# Use a loop to print the name of each country included in the dictionary.

rivers = {
    "nile": "egypt",
    "amazon": "brazil",
    "yangtze": "china",
}

# sentence
for river, country in rivers.items():
    print(f"{river.title()} runs through {country.title()}.")

print("\nHere is name of all rivers in the dictionary:")
for river in rivers: # you can use .keys() here (optional)
    print(river.title())

print("\nHere is name of all countries in the dictionary:")
for country in rivers.values():
    print(country.title())