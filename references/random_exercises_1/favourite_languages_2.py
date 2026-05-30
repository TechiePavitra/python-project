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
        
# plural fix with if else condition and len function
favourite_languages = {
    "jen": ["python", "rust"],
    "sarah": ["c"],
    "edward": ["rust", "go"],
    "phil": ["python", "haskell"],
}

for name, languages in favourite_languages.items():
    if len(languages) > 1:
        print(f"{name.title()}'s favourite languages are listed below:")
        
        for language in languages:
            print(language.title())
        # blank line
        print()
    
    else:
        print(f"{name.title()}'s favourite language is {languages[0].title()}")
        # blank line
        print()

        