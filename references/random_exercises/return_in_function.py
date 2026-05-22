def get_formatted_name(first_name, last_name):
    """Return a Full Name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

actor = get_formatted_name("john", "wick")
print(actor)

# Return is really helpful, it means
# Get the result back from the function.
# Return is not a function, it's a keyword,
# like "if", "else", "for", "in", "not", "or", "and".

# this is not useless, because we will use this
# In large programs, store first and last names separately,
# and call get_formatted_name() to display the full name whenever needed.