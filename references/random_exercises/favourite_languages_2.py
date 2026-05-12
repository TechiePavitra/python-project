# list in a dictionary
# dictionaries each key are unique
print(f"Right Way output Starts here: ")
favourite_languages = {
    # name   languages in list
    "john": ["python", "rust"],
    "neil": ["java", "c"],
    "steve": ["javascript"],
    "alex": ["rust", "c"],
    "mohit": ["c++"],
}

# print out their name and their favourite programming languages
for name, languages in favourite_languages.items():
    print(f"\n{name.title()}'s Favourite Programming Languages are listed below:") 
    
    for language in languages:
        print(f"\t{language.title()}")

# wrong way

favourite_languages = {
    # name   languages in list
    "john": ["python", "rust"],
    "neil": ["java", "c"],
    "steve": ["javascript"],
    "alex": ["rust", "c"],
    "mohit": "c++",
}

# print out their name and their favourite programming languages
for name, languages in favourite_languages.items():
    print(f"\n{name.title()}'s Favourite Programming Languages are listed below:") 
    
    for language in languages:
        print(f"\t{language.title()}")