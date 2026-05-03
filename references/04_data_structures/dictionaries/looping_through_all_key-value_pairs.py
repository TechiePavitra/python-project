user_0 = {
    "username": "techiepavitra",
    "first_name": "pavitra",
    "last_name": "patil",
}

# first variable name for the key
# for value use second variable name using a comma
for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

# favourite languages example
favourite_languages = {
    "michael": "python",
    "jen": "c",
    "steve": "rust",
    "alex": "java",
    "mohit": "javascript",
    "rohan": "assembly",
}

for name, language in favourite_languages.items():
    print(f"{name.title()}'s Favourite Computer Language is {language.title()}.")


