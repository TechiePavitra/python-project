# Make a dictionary called cities. 
# Use the names of three cities as keys in your dictionary. 
# Create a dictionary of information about each city and include the country that the city is in, 
# its approximate population, and one fact about that city. 
# The keys for each city’s dictionary should be something like country, 
# population, and fact. Print the name of each city and all of the information you have stored about it

# dictionary
cities = {
    "surat": {
        "country": "india",
        "population": "6.7 million",
        "fact": "surat is known as diamond city of india",
    },
    "paris": {
        "country": "france",
        "population": "2.1 million",
        "fact": "paris is home to the famous eiffel tower",
    },
    "tokyo": {
        "country": "japan",
        "population": "14 million",
        "fact": "tokyo is the largest metropolitan area in the world",
    },
}

# nested for loop 
for city, info in cities.items():
    print(f"\n{city.title()} Information is given below:")
    
    for key, detail in info.items():
        print(f"\t{key.title()}: {detail.title()}")