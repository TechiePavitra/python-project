# in this example we need to print the name and their favourite programming languages,
# we uses .items() to get both values

favourite_languages = {
#   name (key), language (value)
    "sarah": "python",
    "john": "c",
    "merry": "javascript",
    "mohit": "java",
    "rohit": "ruby",
    "jenny": "c++",
    "anil": "python",
}

favourite_languages["umesh"] = "ruby" # added a new name with their favourite language

# Read (Print) everyones favourite computer languages with their name.
for name, language in favourite_languages.items(): # .items() returns each entry as a (key, value) pair — we unpack both
    print(f"{name.title()}'s Favourite Language is {language.title()}.")

# Why to use this?
for name in favourite_languages.keys():
    print(name.title()) 
        
# instead of this?
for name, language in favourite_languages.items():
    print(name.title())
    
# Answer: in second example we used .items() method which calls keys and values both.
# but we are only using the Key which is name, and throwing the language away from us.
# it's like ordering a combo in a restaurant, but don't touch the other item in combo.
# when you only need keys in a dictionary, use the .keys() method or if you only need values
# use the .values() method, it is better to read and understand, which is way more valuable in programming.

# you can use even shorter code if you want the keys only.
# .keys() method is default behaviour in python so you can omit (remove) the .keys() method.
# it is optional to add .keys() method, for a clean code do not use .keys()
# but the .keys() method is better to understand and clarity, when you want to write professional code
# always omit .keys()
for name in favourite_languages:
    print(name.title())
