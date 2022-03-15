import pdb 
from models.artist import Artist
from models.album import Album
import repositories.artist_repository as artist_repository  
import repositories.album_repository as album_repository

album_repository.delete_all()
artist_repository.delete_all()

artist_1 = Artist("Madonna")
artist_repository.save(artist_1)

album_1 = Album("Greatest Hits" , "Pop" , artist_1)
album_repository.save(album_1)

album_2 = Album("Another Album" , "Pop" , artist_1)
album_repository.save(album_2)

select_artist = artist_repository.select(artist_1.id)
print (select_artist)

select_album = album_repository.select(album_1.id)
print (f"Album title: {select_album.title} , Album Genre: {select_album.genre} , Artist: {select_album.artist.name}")

all_artists = artist_repository.select_all()
for artist in all_artists:
    print(artist)

all_albums= album_repository.select_all()
for album in all_albums:
    print (f"Album title: {album.title} , Album Genre: {album.genre} , Artist: {album.artist.name}")

list_all_albums = album_repository.select_all_albums(artist_1)
for album in list_all_albums:
    print (album.title)

the_beatles = Artist ("The Beatles")
artist_repository.edit_artist(artist_1, the_beatles)

fantastic_album = Album ("Fantastic Album" , "Rock", artist_1)
album_repository.edit_album(album_2, fantastic_album)

album_repository.delete(album_1.id)
album_repository.delete(album_2.id)
artist_repository.delete(artist_1.id)
