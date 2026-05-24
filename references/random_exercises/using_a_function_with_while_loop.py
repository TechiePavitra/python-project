def get_formatted_name(first_name, last_name, middle_name=''):
    """Format usernames"""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name

# This is infinite loop!
while True:
    print("\nPlease tell me your Name  ")
    print("Use 'q' to quit the program")
    
    fname = input("Enter your First name:  ")
    if fname == 'q':
        break
    
    lname = input("Enter your Last name:  ")
    if lname == 'q':
        break
    
    formatted_name = get_formatted_name(fname, lname)
    print(f"Hello, {formatted_name}!")