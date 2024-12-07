class Song:
    # Class attributes
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        """
        Initializes a new Song instance with name, artist, and genre.
        Updates class attributes for tracking counts, genres, and artists.
        """
        self.name = name
        self.artist = artist
        self.genre = genre

        # Increment the song count
        self.add_song_to_count()

        # Add genre and artist
        self.add_to_genres(genre)
        self.add_to_artists(artist)

        # Update genre and artist count histograms
        self.add_to_genre_count(genre)
        self.add_to_artist_count(artist)

    @classmethod
    def add_song_to_count(cls):
        """Increments the count of total songs created."""
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        """Adds a genre to the genres list if it's not already included."""
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        """Adds an artist to the artists list if they're not already included."""
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        """
        Updates the genre_count dictionary to track the number of songs
        per genre.
        """
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artist_count(cls, artist):
        """
        Updates the artist_count dictionary to track the number of songs
        per artist.
        """
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1
