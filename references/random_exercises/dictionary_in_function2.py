def build_person(first_name, last_name, age=None):
    """Store information about a person"""
    person = {
        "fname": first_name,
        "lname": last_name,
    }
    
    if age:
        person['age'] = age
    return person

build_person("pavitra", "patil", 18)

# Falsy:
# False
# None
# 0
# ''      # empty string
# []      # empty list
# {}      # empty 

# Truthy:
# True
# Number other than 0
# 'Non Empty String'
# ['Non Empty String']
# {"name": "john"} non empty dictionary