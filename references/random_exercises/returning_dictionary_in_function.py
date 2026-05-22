def build_person(first_name, last_name):
    """Return a dictionary about person."""
    person = {
        "fname": first_name,
        "lname": last_name,
    }
    return person

print(build_person(first_name="michael", last_name="jackson"))