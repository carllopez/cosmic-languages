import requests


# Lyrics and songs API
MUSIXMATCH_BASE_URL = "https://api.musixmatch.com/ws/1.1/"
MUSIXMATCH_TRACK_LYRICS_GET = "track.lyrics.get?"
MUSIXMATCH_TRACK_LYRICS_SEARCH = "track.search?"


class LyricsClient(object):

    def __init__(self, key):
        self.key = key
        self.base_url = MUSIXMATCH_BASE_URL

    def get(self, method, payload={}):
        if not method:
            return None

        response = requests.get(f"{self.base_url}{method}", params=payload)
        return response

    def search_song(self, title, artist=None):
        payload = {"apikey": self.key, "q_track": title, "q_artist": artist}
        response = self.get(method=MUSIXMATCH_TRACK_LYRICS_SEARCH, payload=payload)
        formatted_response = response.json()
        response_header = formatted_response["message"]["header"]
        response_body = formatted_response["message"]["body"]
        if response_header["status_code"] == 200: # All good, we can work with the response
            track_ids = [track["track"]["track_id"] for track in response_body["track_list"] if track["track"]["has_lyrics"] == 1]
            return track_ids[0] if track_ids else None
        else: # Something happened, return an error
            return "Error when looking up the song"

    def get_lyrics(self, track_id=None):
        if not track_id:
            return "No lyrics found for song"

        payload = {"apikey": self.key, "track_id": track_id}
        response = self.get(method=MUSIXMATCH_TRACK_LYRICS_GET, payload=payload)
        formatted_response = response.json()
        response_header = formatted_response["message"]["header"]
        response_body = formatted_response["message"]["body"]
        if response_header["status_code"] == 200: # All good, we can work with the response
            return self.get_first_lyrics_words(response_body["lyrics"]["lyrics_body"])
        else: # Something happened, return an error
            return "Error when fetching lyrics"

    def get_first_lyrics_words(self, s):
        s = s.replace("\n", " ").split(" ")
        s = list(filter(None, s))
        return s[:100]
