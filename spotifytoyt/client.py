from dotenv import load_dotenv
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
import bs4
import os
import requests
import json


load_dotenv()
SPOTIFY_ID = os.getenv("SPOTIFY_ID")
SPOTIFY_SECRET = os.getenv("SPOTIFY_SECRET")
SPOTIFY_USER_ID = os.getenv("SPOTIFY_USER_ID")
YT_FILE_PATH = os.getenv("YT_FILE_PATH")

class YoutubeHelper():
    # create an API client
    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file_path = YT_FILE_PATH
    scopes = ["https://www.googleapis.com/auth/youtube.force-ssl",
              "https://www.googleapis.com/auth/youtube", "https://www.googleapis.com/auth/youtubepartner"]

    def __init__(self) -> None:
        flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
            self.client_secrets_file_path, self.scopes)
        credentials = flow.run_console()
        self.client = googleapiclient.discovery.build(
            self.api_service_name, self.api_version, credentials=credentials)

    # returns a playlist resource
    def create_playlist(self, title, description, public=True):
        """ creates a new youtube playlist and returns id

            Parameters:
                - title - the title of the playlist
                - description - the description of the playlist
                - public - whether the playlist is public or not
        """
        request = self.client.playlists().insert(
            part="snippet,status",
            body={
                "snippet": {
                    "title": title,
                    "description": description,
                    "defaultLanguage": "en"
                },
                "status": {"privacyStatus": "public" if public else "private"}
            }
        )
        response = request.execute()
        return response["id"]

    def song_search(self, search_item):
        """ scrapes https://www.youtube.com/results?search_query={search_item} for the first video id

            Parameters:
                - search_item - a song name (string) to search for
        """
        url = "https://www.youtube.com/results?search_query=" + search_item
        response = requests.get(url)
        soup = bs4.BeautifulSoup(repr(response.content), 'html.parser')
        results = soup.select(
            "script:-soup-contains('ytInitialData')")[0].text
        if '"ads":[{"promotedVideoRenderer"' in results: # test for ads
            return results.split('"videoId":"')[2].split('"')[0]
        return results.split('"videoId:"')[0].split('"videoId":"')[1].split('"')[0] 

    # playlist id and video id are the same as shown in the url
    def insert_songs(self, playlist_id, video_ids):
        """ inserts a song into a playlist

            Parameters:
                - playlist_id - a youtube playlist id
                - video_id - list of youtube video id
        """
        for video_id in video_ids:
            request = self.client.playlistItems().insert(
                part="snippet",
                body={
                    "snippet": {
                        "playlistId": playlist_id,
                        "resourceId": {
                            "kind": "youtube#video",
                            "videoId": video_id
                        }
                    }
                }
            )
            request.execute()

    def song_ids(self, playlist_id, max_results=1000):
        """ returns a list of song ids from a playlist, no author

            Parameters:
                - playlist_id - a youtube playlist id
                - max_results - the maximum number of results to return
        """
        video_ids = []
        request = self.client.playlistItems().list(
            part="snippet",
            id=playlist_id
        )
        i = 0
        while request:
            response = request.execute()
            for item in response["items"]:
                video_ids.append(item["snippet"]["resourceId"]["videoId"])
                i += 1
                if i > max_results:
                    return video_ids
            request = self.client.playlists().list_next(request, response)
        return video_ids

    def song_names(self, playlist_id, max_results=1000): 
        """ returns a list of song names from a playlist, no author

            Parameters:
                - playlist_id - a youtube playlist id
                - max_results - the maximum number of results to return
        """
        video_names = []
        request = self.client.playlistItems().list(
            part="snippet",
            playlistId=playlist_id
        )
        i = 0
        while request:  # each request seems to have 5 songs
            response = request.execute()
            for item in response["items"]:
                #print(item["snippet"]["title"])
                video_names.append(item["snippet"]["title"])
                i += 1
                if i > max_results:
                    return video_names
            request = self.client.playlists().list_next(request, response)
        return video_names


class SpotifyHelper(spotipy.Spotify):
    def __init__(self):
        #super().__init__(client_credentials_manager=SpotifyClientCredentials(client_id=SPOTIFY_ID, client_secret=SPOTIFY_SECRET))
        super().__init__(auth_manager=SpotifyOAuth(scope="playlist-modify-private playlist-modify-public",
                                                   client_id=SPOTIFY_ID, client_secret=SPOTIFY_SECRET, redirect_uri="http://example.com"))


    def create_playlist(self, title, description, public=True):
        """ creates a new spotify playlist and returns id

            Parameters:
                - title - the title of the playlist
                - description - the description of the playlist
                - public - whether the playlist is pubiic or not
        """
        response = self.user_playlist_create(
            SPOTIFY_USER_ID, name=title, public=public, description=description)
        return response["id"]
    # create playlist is already a method, use user_playlist_create()


    # insert song is already a method, use playlist_add_items()
    def insert_songs(self, playlist_id, song_ids):
        """ inserts a song into a playlist
            Parameters:
                - playlist_id - a spotify playlist id
                - song_ids - a spotify song id
        """
        self.user_playlist_add_tracks(SPOTIFY_USER_ID, playlist_id=playlist_id, tracks=song_ids)

    def song_names(self, playlist_id):
        """ returns a list of song names from a playlist, with format "{song name} {author}"

            Parameters:
                - playlist_id - a spotify playlist id
        """
        playlist = self.playlist(playlist_id)
        page = playlist["tracks"]
        tracks = []
        for track in page["items"]:
            if not track["track"]:
                continue
            tracks.append(track["track"]["name"] + ' ' +
                          track["track"]["artists"][0]["name"])
        while page["next"]:
            page = page["next"]
            for track in page["items"]:
                if not track["track"]:
                    continue
                tracks.append(track["track"]["name"] + ' ' +
                              track["track"]["artists"][0]["name"])
        return tracks

    # 
    def song_ids(self, playlist_id):
        """ returns a list of song ids from a playlist
            id -> url = https://open.spotify.com/track/{id}

            Parameters:
                - playlist_id - a spotify playlist id
        """
        playlist = self.playlist(playlist_id)
        page = playlist["tracks"]
        tracks = []
        for track in page["items"]:
            if not track["track"]:
                continue
            tracks.append(track["track"]["id"])
        while page["next"]:
            page = page["next"]
            for track in page["items"]:
                if not track["track"]:
                    continue
                tracks.append(track["track"]["id"])
        return tracks

    def song_search(self, query):  # song name to song id
        """ returns a song id from a song name
        
            Parameters:
                - query - a song name (string) to search for
        """
        result = self.search(query, limit=1)
        if result["tracks"]["total"] == 0:
            return None
        return result["tracks"]["items"][0]["id"]


# y = YoutubeHelper()
# print(y.song_names("PLwKmMt97VRboQsy9v0nO7NtIZ9FPk1mqq"))
# s = SpotifyHelper()
# s.insert_songs("66rFAZis34nYcd78KtVwKU", ["2Rv0hsvlWB16tCiSKyJW7r"])