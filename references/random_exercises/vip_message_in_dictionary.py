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

vip_members = ["john", "sarah"]

# Here the John and Sarah are VIP and Experienced Engineers.
# for everyone prints normal message while for John and Sarah.
# and than print a special message to VIP Members like "I see you love Python!"
# print a special message to erin who forgot to poll.

# special msg for erin! 
if 'erin' not in favourite_languages.keys():
    print("Erin, please take our poll!")

for name in favourite_languages:
    print(f"Hi {name.title()}.")
   
    if name in vip_members:
        language = favourite_languages[name] 
        print(f"\tI see you love {language.title()}!")

                     
# My Try! through another thing in my mind      
numbers = {
    0: "neither prime nor composite number",
    1: "neither prime nor composite number",
    2: "prime number",
    3: "prime number",
    4: "composite number",
    5: "prime number",
    6: "composite number",
}

for number, information in numbers.items():
    if number in range(0, 7, 2):
        print(f"The Number: {number}")
        print(f"\tInformation: {information.title()}")
        print(f"\tThe Number is an Even Number")
    else:
        print(f"The Number: {number}")
        print(f"\tInformation: {information.title()}")
        print(f"\tThe Number is an Odd Number")

