import json
import requests


MUSIXMATCH_BASE_URL = "https://api.musixmatch.com/ws/1.1/"
MUSIXMATCH_TRACK_LYRICS_GET = "track.lyrics.get?"
MUSIXMATCH_KEY = "b0be994f81a9800e914305c52f237eef"



def get_lyrics(title, artist=None):
    track_temp_id = 15953433

    payload = {"apikey": MUSIXMATCH_KEY, "track_id": track_temp_id}
    response = requests.get(f"{MUSIXMATCH_BASE_URL}{MUSIXMATCH_TRACK_LYRICS_GET}", params=payload)
    print(response.json())


get_lyrics(title="Title")