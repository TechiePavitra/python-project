# Write a function called city_country() that takes in the name of a city and its country. 
# The function should return a string formatted like this:
# "Santiago, Chile"
# Call your function with at least three city-country pairs, 
# and print the values that are returned.

def city_country(city_name, country_name):
    """Returns formatted country and city name"""
    formatted_value = (f"{city_name.title()}, {country_name.title()}")
    return formatted_value

countries = {
    # city    country
    "santiago": "chile",
    "surat": "india",
    "tokyo": "japan",
    "paris": "france",
}

for city, country in countries.items():
    print(city_country(city, country))