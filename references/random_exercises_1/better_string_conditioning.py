mohit = {
    "age": 17,
    "favourite_languages": ["python", "javascript", "css", "html", "c", "rust", "myhtmlcsshub"],
    "city": "surat",
}

# which method is better?

# 1st method 
print("First method starts here: ")
for language in mohit["favourite_languages"]:
    if "html" in language: 
        print(f"The {language.upper()} is mohit's favourite language")
    elif "css" in language:
        print(f"The {language.upper()} is mohit's favourite language")
    else:
        print(f"The {language.title()} is mohit's favourite language")

# this method checks if the "html" is in the key value of favourite_languages.
# look the myhtmlcsshub is also converted in uppercase.
# because there is html and css word in there.
# so this method is not great to use

print("\nSecond method starts here: ")
# 2nd method
for language in mohit["favourite_languages"]:
    if language == "html":
        print(f"The {language.upper()} is mohit's favourite language")
    elif language == "css":
        print(f"The {language.upper()} is mohit's favourite language")
    else:
        print(f"The {language.title()} is mohit's favourite language")

# this method is great, this checks if the "html" = "html" or not.
# if it's "myhtmlcsshub" which is not equal to html than it is not being affected!