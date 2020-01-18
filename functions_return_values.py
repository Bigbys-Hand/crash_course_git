#Return Values are produced when a function takes arguments and performs operations on the raw values to produce new ones.
def get_formatted_titles(book_title, publisher):
    """Return a short blurb about the provided book. Features correctly formatted title and publisher."""
    book_blurb = f"'{book_title.title()}' by {publisher.title()}"
    return book_blurb
#when you call a function that returns a value, you need to set up a variable that the return value can be assigned to.
#this makes the function more programmatically useful.
current_book = get_formatted_titles('A Moveable Feast','ernest hemingway')

#you can deal with uncertainty in the info you might receive by making one or more arguments optional.
def get_formatted_author(first_name, last_name, best_book, middle_name=''):
    """Returns an author's name and title of a book of theirs, properly formatted. Handles middle names or their absence."""
    if middle_name:
        name_and_book = f"{first_name.title()} {middle_name.title()} {last_name.title()} is best known for '{best_book.title()}'"
    else:
        name_and_book = f"{first_name.title()} {last_name.title()} is best known for '{best_book.title()}'"
    return name_and_book
#the return clause is fed the product of the operations run on the raw arguments, 'name_and_book'.        
author_blurb = get_formatted_author('Charles','Lewis','the chronicles of narnia')
print(author_blurb)

def make_album(artist_name, album_title, song_count=None):
    artist = {'name':artist_name,'title':album_title}
    if song_count:
        artist['songs'] = song_count
    return artist

while True:
    print("\n Enter your favorite musician and their best album:")
    artist_name = input("Artist name: ")
    if artist_name == 'q':
        break
    album_title = input("Best album: ")
    if album_title == 'q':
        break
    
    name_and_album = f"{artist_name.title()}, '{album_title.title()}'"
    print(f"\n filler text {name_and_album}")
    
