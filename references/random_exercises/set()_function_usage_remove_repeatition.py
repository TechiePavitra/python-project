favourite_languages = {
    "michael": "python",
    "john": "javascript", 
    "steve": "c", 
    "alex": "python", 
    "jimmy": "c", 
    "umesh": "javascript", 
    "dinesh": "c++", 
    "mohit": "java", 
}

# Every Languages that is in this poll.
# set function combines same value and display only one
# here the python is favourite of Michael and alex, to display and simplify
# we used set function, to display how many languages does people's favourite, 
# and listed here
for language in sorted(set(favourite_languages.values())):
    print(language.title())

# wrong way to do, always use sorted first than set,
# for language in set(sorted(favourite_languages.values())):
# because set destroys the sorted function
