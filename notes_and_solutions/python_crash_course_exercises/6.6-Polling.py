# Use the code in favorite_languages.py (page 96).
# Make a list of people who should take the favorite languages poll. 
# Include some names that are already in the dictionary and some that are not.
# Loop through the list of people who should take the poll. 
# If they have already taken the poll, print a message thanking them for responding.
# If they have not yet taken the poll, print a message inviting them to take the poll.

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

# List of people who should take the poll
poll_list = ['jen', 'sarah', 'david', 'mike', 'edward']

# Loop through the list
for person in poll_list:
    if person in favorite_languages:
        print(f"Hey {person.title()}, Thank you! for taking the poll.")
    else:
        print(f"Hello {person.title()}, can you please take this poll.")