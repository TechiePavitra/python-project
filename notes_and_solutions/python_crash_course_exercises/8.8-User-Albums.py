# start with your program from Exercise 8-7. 
# Write a while loop that allows users to enter an album’s artist and title.
# Once you have that information, call make_album() with the user’s input and print the dictionary that’s created. 
# Be sure to include a quit value in the while loop.

def make_album(artist_name, album_title):
    """Make a album dictionary containing artist name and album title."""
    album = {"artist_name": artist_name, "album_title": album_title}
    return album

while True:
    print("\nUse 'quit' to exit this program:")
    
    artist_name_input = input("Enter your artist name:  ") 
    if artist_name_input == 'quit':
        break
    
    artist_title_input = input("Enter your artist title:  ") 
    if artist_title_input == 'quit':
        break
    
    new_artist = make_album(artist_name_input, artist_title_input)
    print(new_artist)

# Note: i used break, because this program is simple.
# but in complex program always use flags 