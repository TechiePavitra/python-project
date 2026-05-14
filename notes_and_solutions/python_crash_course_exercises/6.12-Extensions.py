# We’re now working with examples that are complex enough that they can be extended in any number of ways. 
# Use one of the example programs from this chapter, 
# and extend it by adding new keys and values, 
# changing the context of the program, 
# or improving the formatting of the output.

# Let's Extend 6.11 Exercise
cities = {
    "surat": {
        "country": "india",
        "population": "6.7 million",
        "fact": "surat is known as diamond city of india",
        "languages": "gujarati",
        "foods": "locho",
        "currency": "indian rupees",
    },
    "paris": {
        "country": "france",
        "population": "2.1 million",
        "fact": "paris is home to the famous eiffel tower",
        "languages": "french",
        "foods": "baguette",   
        "currency": "euro",
    },
    "tokyo": {
        "country": "japan",
        "population": "14 million",
        "fact": "tokyo is the largest metropolitan area in the world",
        "languages": "japanese",
        "foods": "sushi", 
        "currency": "japanese yen",   
    },
}

# nested for loop 
for city, info in cities.items():
    print(f"\n{city.title()} Information is given below:")
    
    for key, detail in info.items():
        print(f"\t{key.title()}: {detail.title()}")