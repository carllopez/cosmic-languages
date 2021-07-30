import json
import requests


MUSIXMATCH_BASE_URL = "https://api.musixmatch.com/ws/1.1/"
MUSIXMATCH_TRACK_LYRICS_GET = "track.lyrics.get?"
MUSIXMATCH_KEY = "b0be994f81a9800e914305c52f237eef"



def get_lyrics(title, artist=None):
    track_temp_id = 15953433

    payload = {"apikey": MUSIXMATCH_KEY, "track_id": track_temp_id}
    response = requests.get(f"{MUSIXMATCH_BASE_URL}{MUSIXMATCH_TRACK_LYRICS_GET}", params=payload)
    formatted_response = response.json()
    response_header = formatted_response["message"]["header"]
    response_body = formatted_response["message"]["body"]
    if response_header["status_code"] == 200: # All good, we can work with the response
        return response_body["lyrics"]["lyrics_body"]
    else: # Something happened, return an error
        return "Error when looking up the song"


get_lyrics(title="Title")