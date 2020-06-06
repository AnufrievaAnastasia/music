from main import *

album = Album("Bob's First Single", '2:45',  '2001')
album.add_song("A Ballad about Cheese", '2:45', 'dfdf', '2001')
album.add_song("1", '2', '3', '4')
band = Album("Bob's First Single1234", '2:45',  '2001')
band.add_song("12", '22', '32', '42')

print(album.songs)

