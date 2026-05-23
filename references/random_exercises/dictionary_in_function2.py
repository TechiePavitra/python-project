def build_person(first_name, last_name, age=None):
    """Store information about a person"""
    person = {
        "fname": first_name,
        "lname": last_name,
    }
    
    if age:
        person['age'] = age
    return person

build_person("pavitra", "patil", 52)