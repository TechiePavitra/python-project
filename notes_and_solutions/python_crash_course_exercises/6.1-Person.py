# Use a dictionary to store information about a person you know. 
# Store their first name, last name, age, and the city in which they live. 
# You should have keys such as first_name, last_name, age, and city. 
# Print each piece of information stored in your dictionary.

person = {
    "first_name": "michael",
    "last_name": "jackson",
    "age": 50, # when he died
    "city": "los angeles", 
}

# i have added variable for more readable print / optional
first_name = person["first_name"]
last_name = person["last_name"]
age = person["age"]
city = person["city"]

print(f"First Name: {first_name.title()}")
print(f"Last Name: {last_name.title()}")
print(f"Age: {age}")
print(f"City: {city.title()}")