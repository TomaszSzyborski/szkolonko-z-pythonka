"""
Stworz 4 klasy:

    Song - ma zawierać
        title
        artist -> Artist
        album
        track_number
        time -> time ma być property (getter, setter) który jeśli piosenka będzie dluższa niz 5m ustawi na 5 min

        artyscie dodać automatycznie Song (podpowiedz mozna przekazać samego siebie)

    Album
        title
        artist
        year
        tracks = [] lista Song

        artyscie dodać automatycznie Album (podpowiedz mozna przekazać samego siebie)

        funtion
            add_track(title, time, artist=None)
                - jesli artist jest None przypisz użyj Album artist
                - sprawdz ile piosenek jest w tracks
                - stworz obiekt Song(title, artist, self, track_number, time)
                - dodaj song do tracks Albumu


    Artist
        name
        albums = []
        songs = []

        function
            add_album(self, album)
                - dodac album do albums
            add_song(self, song)
                dodac song do songs

            __str__ - wypisanie albumów i piosenek jako string

    Playlist
        name
        songs = []

        function
            add_song(self, song)
                dodanie piosenki do songs
            add_album(self, album)
                dodanie wszystkich piosenek z albumu do songs
            property artists - lista artystów z piosenek(tylko getter)
            property albums - lista albumów z piosenek(tylko getter)




"""


class Song:
    def __init__(self, title, artist: "Artist", album, track_number, time):
        print(f"Tworzenie Song({title}, {artist}, {album}, {track_number})")
        self.title = title
        self.artist = artist
        self.album = album
        self.track_number = track_number
        self.time = time

        self.artist.add_song(self)

    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, value):
        if value > 300:
            value = 300
        self._time = value

    def __str__(self):
        return f'Song: {self.title}'

    def __repr__(self):
        return f'Song: {self.title}'


class Album:

    def __init__(self, title, artist, year):
        print(f"Tworzenie Albumu({title}, {artist}, {year})")
        self.title = title
        self.artist = artist
        self.year = year
        self.tracks = []
        self.artist.add_album(self)

    def add_track(self, title, time, artist=None):
        print(f"Dodanie Piosenki({title}) do Albumu({self.title}, {self.artist}, {self.year})")
        if artist == None:
            artist = self.artist
        track_number = len(self.tracks) + 1
        song = Song(title, artist, self, track_number, time)
        self.tracks.append(song)

        print(f"Albumu({self.title}, {self.artist}, {self.year}) Tracks -> {self.tracks}")

    def __str__(self):
        return f'Albums: {self.title}'

    def __repr__(self):
        return f'Albums: {self.title}'


class Artist:
    def __init__(self, name):
        print(f"Tworzenie Artysty({name})")
        self.name = name
        self.albums = []
        self.songs = []

    def add_album(self, album):
        self.albums.append(album)
        print(f"Dodanie Albumu({album.title})")

    def add_song(self, song):
        self.songs.append(song)
        print(f"Dodanie Song({song.title})")

    def __str__(self):
        return f'{self.name} Albums: {self.albums}, Songs: {self.songs}'

    def __repr__(self):
        return f'{self.name} Albums: {self.albums}, Songs: {self.songs}'


band = Artist("Bob's Awesome Band")
album = Album("Bob's First Single", band, 2013)
album = Album("New Album", band, 2015)
print(band)
for album in band.albums:
    print(f'{album.title}, {album.year}')

# album.add_track("A Ballad about Cheese", 5 * 60)
# album.add_track("A Ballad about Cheese (dance remix)", 6 * 60)
# album.add_track("A Third Song to Use Up the Rest of the Space", 3 * 60)
# print(band)

# queen = Artist("Queen")
# album_sheer = Album("Sheer Heart Attack", band, 1991)
# album_sheer.add_track("Brighton Rock", 5*60)
# album_sheer.add_track("Flick of the Wrist", 6*60)
# album_sheer.add_track("Lily of the Valley", 3*60)

# playlist = Playlist("My Favourite Songs")

# for song in album.tracks:
#     playlist.add_song(song)

# playlist.add_album(album_sheer)

# print(f"Playlist songs={playlist.songs}")
# print(f"Playlist artists={playlist.artists}")
# print(f"Playlist Albums={playlist.Albums}")

