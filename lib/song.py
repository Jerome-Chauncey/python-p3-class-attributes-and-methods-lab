class Song:

    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre


        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        if genre in Song.genre_count:
            Song.genre_count[genre] += 1
        else:
            Song.genre_count[genre] = 1

    @classmethod
    def add_to_artist_count(cls, artist):
        if artist in Song.artist_count:
            Song.artist_count[artist] += 1
        else:
            Song.artist_count[artist] = 1

    
    


        # Song.count += 1
        # Song.genres.append(genre)
        # Song.artists.append(artist)

        # if genre in Song.genre_count:
        #     Song.genre_count[genre] += 1
        # else:

        #     Song.genre_count[genre] = 1

        # if artist in Song.artist_count:
        #     Song.artist_count[artist] += 1
        # else:
        #     Song.artist_count[artist] = 1


    
        


    
        





ninety_nine_problems = Song("99 Problems", "Jay-Z", "Rap")
spooky = Song("Spooky", "PRXNCE", "Kenyan/Swiss")
lie_to_me = Song("Lie To Me", "Karun, Blocka", "Kenyan/House")
v_6 = Song("V6", "Malie Donn", "Dancehall")


print(f"Song Count : {Song.count}")
print(f"Song Genres: {Song.genres}")
print(f"Song Artists: {Song.artists}")
print(f"Genre Count: {Song.genre_count}")
print(f"Artist Count: {Song.artist_count}")







# print(f"Song Name: {ninety_nine_problems.name}")
# print(f"Artist Name: {ninety_nine_problems.artist}")
# print(f"Song Genre: {ninety_nine_problems.genre}")

# print(f"Song Name: {spooky.name}")
# print(f"Artist Name: {spooky.artist}")
# print(f"Song Genre: {spooky.genre}")

# print(f"Song Name: {lie_to_me.name}")
# print(f"Artist Name: {lie_to_me.artist}")
# print(f"Song Genre: {lie_to_me.genre}")

# print(f"Song Name: {v_6.name}")
# print(f"Artist Name: {v_6.artist}")
# print(f"Song Genre: {v_6.genre}")


# print(f"Song Count: {ninety_nine_problems.count}")
# print(f"All Genres: {Song.genres}")
# print(f"All Artists: {Song.artists}")
# print(Song.genre_count)
# print(Song.artist_count)


