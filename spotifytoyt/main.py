# code for creating a spotify playlist from a youtube playlist and vice versa
# can do yt -> yt and spotify -> spotify too but i think spotify already has in built
# yt -> yt is useful for mixes, but note that mixes are "customised" based on account you log in with, i.e the acc you choose to give access to (not owner of project)
# mixes also change a bit every time

import client




def spotify_playlist_url(id):
    return f"https://open.spotify.com/playlist/{id}"


def spotify_song_url(id):
    return f"https://open.spotify.com/track/{id}"


def yt_playlist_url(id):
    return f"https://www.youtube.com/playlist?list={id}"


def yt_song_url(id):
    return f"https://www.youtube.com/watch?v={id}"

    
def example_spotify_to_youtube(playlist_id, title="test", public=True): # example
    spotify = client.SpotifyHelper()
    yt = client.YoutubeHelper()
    # get song names from spotify playlist
    names = spotify.song_names(playlist_id)
    # get youtube video ids from song names
    ids = [yt.song_search(name) for name in names] # youtube search will never return none
    # create youtube playlist
    yt_playlist_id = yt.create_playlist(title, f"stolen from {spotify_playlist_url(playlist_id)}", public)
    # add to youtube playlist
    yt.insert_songs(yt_playlist_id, ids)
    # return youtube playlist url
    return yt_playlist_url(yt_playlist_id)


def example_youtube_to_spotify(playlist_id, title="test", public="True"): # example
    yt = client.YoutubeHelper()
    spotify = client.SpotifyHelper()
    # get song names from youtube playlist
    names = yt.song_names(playlist_id)
    # get spotify song ids from song names
    ids = []
    for name in names:
        id = spotify.song_search(name)
        # print(id)
        if id: # spotify search on the other hand...
            ids.append(id)
    # print(ids)
    # create spotify playlist
    spotify_playlist_id = spotify.create_playlist(title, "stolen from {yt_playlist_url(playlist_id)}")
    # add to spotify playlist
    spotify.insert_songs(spotify_playlist_id, ids)
    # return spotify playlist url
    return spotify_playlist_url(spotify_playlist_id)

def main():
    
    #yt = YtHelper()
    # spotify = client.SpotifyHelper()
    # names = spotify.song_names("4VmFt9QWKcOQM31P3xAJSC")
    # spot_url = f"https://open.spotify.com/playlist/{id}"
    print(example_spotify_to_youtube("4YKSlhizzPScnig1NZ6f1k", "25ji", "true"))


if __name__ == "__main__":
    main()
