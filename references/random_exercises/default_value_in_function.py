def build_person(first_name, last_name, age=None):
    """Generates person information."""
    person = {
        "fname": first_name,
        "lname": last_name,
    }
    
    if age:
        person['age'] = age
    return person

print(build_person("pavitra", "patil", 18))