import random
import time

class Song:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration
        self.play_count = 0
        self.story = None
        self.next = None
        self.prev = None

class SongDatabase:
    def __init__(self):
        self.songs = []
        self.database()

    def database(self):

        self.songs.append(Song("Song 1", "Artist 1", 200))
        self.songs.append(Song("Song 2", "Artist 2", 250))
        self.songs.append(Song("Song 3", "Artist 1", 180))
        self.songs.append(Song("Song 4", "Artist 3", 300))
        self.songs.append(Song("Song 5", "Artist 2", 240))
        self.songs.append(Song("Song 6", "Artist 4", 220))
        self.songs.append(Song("Song 7", "Artist 5", 260))
        self.songs.append(Song("Song 8", "Artist 6", 210))
        self.songs.append(Song("Song 9", "Artist 7", 230))
        self.songs.append(Song("Song 10", "Artist 8", 280))
        self.songs.append(Song("Song 11", "Artist 9", 190))
        self.songs.append(Song("Song 12", "Artist 10", 300))
        self.songs.append(Song("Song 13", "Artist 11", 240))
        self.songs.append(Song("Song 14", "Artist 12", 220))
        self.songs.append(Song("Song 15", "Artist 13", 250))
        self.songs.append(Song("Song 16", "Artist 14", 210))
        self.songs.append(Song("Song 17", "Artist 15", 260))
        self.songs.append(Song("Song 18", "Artist 16", 230))
        self.songs.append(Song("Song 19", "Artist 17", 200))
        self.songs.append(Song("Song 20", "Artist 18", 240))

    def show_songs(self):
        print("\nAvailable Songs in Database:")
        print("="*100)
        print(f"{'SONG NO':<30}  {'TITLE':<30} {'ARTIST':<30} {'DURATION'}")
        for index, song in enumerate(self.songs):
            print(f"{index + 1:<30} {song.title:<30} {song.artist:<30} {song.duration:}s")
        print("="*100)

    def get_song_by_serial(self, serial):
        if 1 <= serial <= len(self.songs):
            return self.songs[serial - 1]
        else:
            return None

class MusicPlaylist:
    def __init__(self, name="My Playlist"):
        self.head = None
        self.current_song = None
        self.recently_played = []
        self.history_stack = []
        self.favorite_songs = []
        self.playlist_name = name

    def set_playlist_name(self, name):
        self.playlist_name = name

    def add_song(self,title, artist, duration):
        print()
        new_song = Song(title, artist, duration)
        if not self.head:
            self.head = new_song
            new_song.next = new_song
            new_song.prev = new_song
        else:
            last_song = self.head.prev
            last_song.next = new_song
            new_song.prev = last_song
            new_song.next = self.head
            self.head.prev = new_song
        self.history_stack.append(("add", new_song))
        print(f"Added: {title} by {artist}")

    def remove_song(self, title):
        print()
        if not self.head:
            return
        current = self.head
        while True:
            if current.title == title:
                if current.next == current:
                    self.head = None
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                    if current == self.head:
                        self.head = current.next
                self.history_stack.append(("remove", current))
                print(f"Removed: {title}")
                break
            current = current.next
            if current == self.head:
                print(f"{title} not found in playlist")
                break

    def play(self):
        print()
        if not self.head:
            print("Playlist is empty")
            return
        if not self.current_song:
            self.current_song = self.head
        while self.current_song:
            print(f"Now playing: {self.current_song.title} by {self.current_song.artist}")
            self.current_song.play_count += 1
            self.recently_played.append(self.current_song)
            if len(self.recently_played) > 5:
                self.recently_played.pop(0)
            time.sleep(min(self.current_song.duration, 2))
            self.current_song = self.current_song.next
            if self.current_song == self.head:
                break

    def show_playlist(self):
        if not self.head:
            print("Playlist is empty")
            return
        print()
        print(f"Playlist: {self.playlist_name}")
        current = self.head
        print()
        print("="*100)
        print(f"{'TITLE':<30} {'ARTIST':<30} {'DURATION (in sec)':<30} {'PLAY COUNT'}")
        print()
        while True:
            print(
                f"{current.title:<30} {current.artist:<30} {current.duration:<30} {current.play_count} times"
            )
            current = current.next
            if current == self.head:
                break

    def shuffle(self):
        print()
        if not self.head:
            return
        songs = []
        current = self.head
        while True:
            songs.append(current)
            current = current.next
            if current == self.head:
                break
        random.shuffle(songs)
        self.head = songs[0]
        for i in range(len(songs)):
            songs[i].next = songs[(i + 1) % len(songs)]
            songs[i].prev = songs[i - 1]
        self.current_song = self.head
        print("Playlist shuffled\n")

        self.show_playlist()

    def add_to_favorites(self, title):
        print()
        current = self.head
        while True:
            if current.title == title:
                self.favorite_songs.append(current)
                print(f"{title} added to favorites")
                break
            current = current.next
            if current == self.head:
                print(f"{title} not found in playlist")
                break

    def remove_from_favorites(self, title):
        print()
        for song in self.favorite_songs:
            if song.title == title:
                self.favorite_songs.remove(song)
                print(f"{title} removed from favorites")
                return
        print(f"{title} not found in favorites")

    def show_favorites(self):
        print()
        if not self.favorite_songs:
            print("No favorite songs")
        else:
            print("Favorite songs:")
            print("="*100)
            print(f"{'TITLE':<30} {'ARTIST':<30} {'DURATION (in sec)':<30} {'PLAY COUNT'}")
            for song in self.favorite_songs:
              print(f"{song.title:<30} {song.artist:<30} {song.duration:<30} {song.play_count} times")

    def search_song(self, title):
        print()
        if not self.head:
            print("Playlist is empty")
            return
        current = self.head
        while True:
            if current.title == title:
                print(f"Found: {title} by {current.artist}")
                return
            current = current.next
            if current == self.head:
                print(f"{title} not found in playlist")
                break

    def show_songs_by_artist(self, artist_name):
        print()
        if not self.head:
            print("Playlist is empty.")
            return

        found = False
        current = self.head
        print()
        print(f"Songs by {artist_name}:")
        while True:
            if current.artist.lower() == artist_name.lower():
                print(f"title:{current.title} | (Duration: {current.duration} seconds)")
                found = True
            current = current.next
            if current == self.head:
                break

        if not found:
            print(f"No songs found by artist: {artist_name}")

    def show_recently_played(self):
        print()
        if not self.recently_played:
            print("No recently played songs.")
            return
        print("\nRecently Played Songs:")
        for song in self.recently_played:
            print(f"{song.title} by {song.artist} ({song.duration}s) | Played {song.play_count} times")

    def undo(self):
        print()
        if not self.history_stack:
            print("No actions to undo")
            return
        action, song = self.history_stack.pop()
        if action == "add":
            self.remove_song(song.title)
        elif action == "remove":
            self.add_song(song.title, song.artist, song.duration)

        self.show_playlist()

    def add_story_to_song(self, title, story):
        if not self.head:
            print("Playlist is empty")
            return
        current = self.head
        while True:
            if current.title == title:
                current.story = story
                print(f"Story added to {title}: {story}")
                return
            current = current.next
            if current == self.head:
                print(f"{title} not found in playlist")
                break

    def show_story(self, title):
        if not self.head:
            print("Playlist is empty")
            return
        current = self.head
        while True:
            if current.title == title:
                if current.story:
                    print(f"Story for {title}: {current.story}")
                else:
                    print(f"No story found for {title}")
                return
            current = current.next
            if current == self.head:
                print(f"{title} not found in playlist")
                break

    def sort_playlist(self, by):
        if not self.head:
            print("Playlist is empty. Cannot sort.")
            return
        songs = []
        current = self.head
        while True:
            songs.append(current)
            current = current.next
            if current == self.head:
                break

        if by == 'title':
            songs.sort(key=lambda song: song.title.lower())
        elif by == 'artist':
            songs.sort(key=lambda song: song.artist.lower())
        elif by == 'duration':
            songs.sort(key=lambda song: song.duration)
        elif by == 'play_count':
            songs.sort(key=lambda song: song.play_count, reverse=True)
        else:
            print("Invalid sort criterion. Use 'title', 'artist', 'duration', or 'play_count'.")
            return

        self.head = songs[0]
        for i in range(len(songs)):
            songs[i].next = songs[(i + 1) % len(songs)]
            songs[i].prev = songs[i - 1]
        print(f"\nPlaylist sorted by {by}")
        print("="*100)
        print(f"{'TITLE':<30} {'ARTIST':<30} {'DURATION':<30} {'PLAY COUNT'}")
        for song in songs:
            print(f"{song.title:<30} {song.artist:<30} {song.duration:<30} {song.play_count} times")

    def display_sorted_by_play_count(self):
        if not self.head:
            print("Playlist is empty. Cannot sort.")
            return

        songs = []
        current = self.head
        while True:
            songs.append(current)
            current = current.next
            if current == self.head:
                break

        songs.sort(key=lambda song: song.play_count, reverse=True)

        print("\nPlaylist sorted by play count:")
        print("="*100)
        print(f"{'TITLE':<30} {'ARTIST':<30} {'DURATION':<30} {'PLAY COUNT'}")
        for song in songs:
            print(f"{song.title:<30} {song.artist:<30} {song.duration:<30} {song.play_count} times")

class PlaylistManager:
    def __init__(self):
        self.playlists = {}
        self.current_playlist = None
        self.song_database = SongDatabase()

    def create_playlist(self, name):
        if name in self.playlists:
            print("A playlist with this name already exists.")
        else:
            playlist = MusicPlaylist(name)
            self.playlists[name] = playlist
            print(f"Playlist '{name}' created.")

    def switch_playlist(self, name):
        if name in self.playlists:
            self.current_playlist = self.playlists[name]
            print(f"Switched to playlist: {name}")
        else:
            print(f"No playlist found with the name '{name}'.")

    def show_playlists(self):
        if not self.playlists:
            print("No playlists available.")
        else:
            print("Available Playlists:")
            for name in self.playlists:
                print(f"- {name}")

    def gather_songs_from_playlists(self, playlist_names):
        songs = []
        for name in playlist_names:
            if name in self.playlists:
                playlist = self.playlists[name]
                current = playlist.head
                if current:
                    while True:
                        songs.append(current)
                        current = current.next
                        if current == playlist.head:
                            break
            else:
                print(f"No playlist found with the name '{name}'.")
        return songs

    def shuffle_play_combined_playlists(self, playlist_names):
        print(f"\nShuffling and playing songs from {playlist_names}:")
        songs = self.gather_songs_from_playlists( playlist_names)

        if not songs:
            print("No songs found in the selected playlists.")
            return

        random.shuffle(songs)

        print
        print("="*100)
        print(f"{'TITLE':<30} {'ARTIST':<30} {'DURATION (in sec)':<30} {'PLAY COUNT'}")
        for song in songs:
            print(f"{song.title:<30} {song.artist:<30} {song.duration:<30} {song.play_count} times")

        for song in songs:
            print(f"Now playing: {song.title} by {song.artist}")
            song.play_count += 1
            time.sleep(min(song.duration, 2))

    def change_playlist_name(self):
        if not self.playlists:
            print("No playlists available to rename.")
            return

        self.show_playlists()
        name = input("Enter the name of the playlist you want to change: ")

        if name not in self.playlists:
            print(f"No playlist found with the name '{name}'.")
            return

        new_name = input("Enter the new name for the playlist: ")

        if new_name in self.playlists:
            print("A playlist with this name already exists.")
            return

        self.playlists[new_name] = self.playlists.pop(name)
        self.playlists[new_name].set_playlist_name(new_name)
        print(f"Playlist name changed from '{name}' to '{new_name}'.")

    def display_main_menu(self):
      print("\nMain Menu:")
      print("1: Create a new playlist")
      print("2: Switch to an existing playlist")
      print("3: Show all playlists")
      print("4: Change playlist name")
      print("5: Shuffle playlists")
      print("0: Exit")

    def display_playlist_menu(self):
        print(f"\n{self.current_playlist.playlist_name} - Playlist Menu:")
        print("1: Manage Songs")
        print("2: Playback Options")
        print("3: Favorites")
        print("4: Search & Filter")
        print("5: Additional Features")
        print("e: Exit current playlist")

    def display_song_management_menu(self):
        print("\nSong Management:")
        print("1: Add a song")
        print("2: Remove a song")
        print("3: Show the playlist")
        print("4: Sort playlist")
        print("5: sort by play_count")
        print("6: Shuffle playlist")
        print("b: Back to Playlist Menu")

    def display_playback_options_menu(self):
        print("\nPlayback Options:")
        print("1: Play entire playlist")
        print("2: Play a selected song")
        print("3: Show recently played")
        print("b: Back to Playlist Menu")

    def display_favorites_menu(self):
        print("\nFavorites:")
        print("1: Add to favorites")
        print("2: Show favorites")
        print("b: Back to Playlist Menu")

    def display_search_filter_menu(self):
        print("\nSearch & Filter:")
        print("1: Search song")
        print("2: Show songs by artist")
        print("b: Back to Playlist Menu")

    def display_additional_features_menu(self):
        print("\nAdditional Features:")
        print("1: Add story to a song")
        print("2: Show story of a song")
        print("3: Undo")
        print("b: Back to Playlist Menu")

    def run(self):
        while True:
            if self.current_playlist:
                self.display_playlist_menu()
                choice = input("Enter your choice: ")

                if choice == '1':

                    while True:
                        self.display_song_management_menu()
                        sub_choice = input("Enter your choice: ")
                        if sub_choice == '1':
                            self.song_database.show_songs()
                            serial = int(input("Enter the song number to add: "))
                            song = self.song_database.get_song_by_serial(serial)
                            self.current_playlist.add_song(song.title, song.artist, song.duration)
                        elif sub_choice == '2':
                            self.current_playlist.show_playlist()
                            title = input("Enter the song title to remove: ")
                            self.current_playlist.remove_song(title)
                        elif sub_choice == '3':
                            self.current_playlist.show_playlist()
                        elif sub_choice == '4':
                            sort_by = input("Enter sort criterion ('title', 'artist', 'duration', 'play_count'): ")
                            self.current_playlist.sort_playlist(sort_by)
                        elif sub_choice == '5':
                            self.current_playlist.display_sorted_by_play_count()
                        elif sub_choice == '6':
                            self.current_playlist.shuffle()
                        elif sub_choice == 'b':
                            break
                        else:
                            print("Invalid choice. Please select a valid option.")

                elif choice == '2':

                    while True:
                        self.display_playback_options_menu()
                        sub_choice = input("Enter your choice: ")
                        if sub_choice == '1':
                            self.current_playlist.play()
                        elif sub_choice == '2':
                            title = input("Enter song title to play: ")
                            self.current_playlist.play_selected_song(title)
                        elif sub_choice == '3':
                            self.current_playlist.show_recently_played()
                        elif sub_choice == 'b':
                            break
                        else:
                            print("Invalid choice. Please select a valid option.")

                elif choice == '3':

                    while True:
                        self.display_favorites_menu()
                        sub_choice = input("Enter your choice: ")
                        if sub_choice == '1':
                            title = input("Enter song title to add to favorites: ")
                            self.current_playlist.add_to_favorites(title)
                        elif sub_choice == '2':
                            self.current_playlist.show_favorites()
                        elif sub_choice == 'b':
                            break
                        else:
                            print("Invalid choice. Please select a valid option.")

                elif choice == '4':

                    while True:
                        self.display_search_filter_menu()
                        sub_choice = input("Enter your choice: ")
                        if sub_choice == '1':
                            title = input("Enter song title to search: ")
                            self.current_playlist.search_song(title)
                        elif sub_choice == '2':
                            artist_name = input("Enter artist name: ")
                            self.current_playlist.show_songs_by_artist(artist_name)
                        elif sub_choice == 'b':
                            break
                        else:
                            print("Invalid choice. Please select a valid option.")

                elif choice == '5':

                    while True:
                        self.display_additional_features_menu()
                        sub_choice = input("Enter your choice: ")
                        if sub_choice == '1':
                            title = input("Enter song title to add story to: ")
                            story = input("Enter the story: ")
                            self.current_playlist.add_story_to_song(title, story)
                        elif sub_choice == '2':
                            title = input("Enter song title to show story for: ")
                            self.current_playlist.show_story(title)
                        elif sub_choice == '3':
                            self.current_playlist.undo()
                        elif sub_choice == 'b':
                            break
                        else:
                            print("Invalid choice. Please select a valid option.")

                elif choice == 'e':
                    print("Exiting current playlist")
                    self.current_playlist = None

                elif choice == '0':
                    print("Exiting Playlist Manager.")
                    break

                else:
                    print("Invalid choice. Please select a valid option.")

            else:
                self.display_main_menu()
                choice = input("Enter your choice: ")

                if choice == '1':
                    name = input("Enter the name for the new playlist: ")
                    self.create_playlist(name)
                elif choice == '2':
                    name = input("Enter the name of the playlist to switch to: ")
                    self.switch_playlist(name)
                elif choice == '3':
                    self.show_playlists()
                elif choice == '4':
                    self.change_playlist_name()
                elif choice == '5':
                    self.show_playlists()
                    playlist_names = input("Enter playlist names separated by commas: ").split(",")
                    playlist_names = [name.strip() for name in playlist_names]
                    self.shuffle_play_combined_playlists(playlist_names)
                elif choice == '0':
                    print("Exiting Playlist Manager.")
                    break
                else:
                    print("Invalid choice. Please select a valid option.")


manager = PlaylistManager()
manager.run()