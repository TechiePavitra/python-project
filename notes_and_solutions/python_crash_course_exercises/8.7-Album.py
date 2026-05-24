# Write a function called make_album() that builds a dictionary describing a music album. 
# The function should take in an artist name and an album title, 
# and it should return a dictionary containing these two pieces of information.
# Use the function to make three dictionaries representing different albums.
# Print each return value to show that the dictionaries are storing the album information correctly.

def make_album(artist_name, album_title):
    """Make a album dictionary containing artist name and album title."""
    album = {"artist_name": artist_name, "album_title": album_title}
    return album

artists = [
    make_album("Michael Jackson", "Billie Jean"),
    make_album("Justin bieber", "Baby"),
    make_album("Alan Walker", "Faded"),
]

for artist_data in artists:
    print(artist_data)