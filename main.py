import json
import requests

# Lyrics and songs API
MUSIXMATCH_BASE_URL = "https://api.musixmatch.com/ws/1.1/"
MUSIXMATCH_TRACK_LYRICS_GET = "track.lyrics.get?"
MUSIXMATCH_TRACK_LYRICS_SEARCH = "track.search?"
MUSIXMATCH_KEY = "b0be994f81a9800e914305c52f237eef"

# Dictionary API
DICTIONARY_BASE_URL = "https://api.dictionaryapi.dev/api/v2/entries/en_US/"


def search_song(title, artist=None):
    payload = {"apikey": MUSIXMATCH_KEY, "q_track": title, "q_artist": artist}
    response = requests.get(f"{MUSIXMATCH_BASE_URL}{MUSIXMATCH_TRACK_LYRICS_SEARCH}", params=payload)
    formatted_response = response.json()
    response_header = formatted_response["message"]["header"]
    response_body = formatted_response["message"]["body"]
    if response_header["status_code"] == 200: # All good, we can work with the response
        track_ids = [track["track"]["track_id"] for track in response_body["track_list"] if track["track"]["has_lyrics"] == 1]
        return track_ids[0] if track_ids else None
    else: # Something happened, return an error
        return "Error when looking up the song"


def get_lyrics(track_id=None):
    if not track_id:
        return "No lyrics found for song"

    payload = {"apikey": MUSIXMATCH_KEY, "track_id": track_id}
    response = requests.get(f"{MUSIXMATCH_BASE_URL}{MUSIXMATCH_TRACK_LYRICS_GET}", params=payload)
    formatted_response = response.json()
    response_header = formatted_response["message"]["header"]
    response_body = formatted_response["message"]["body"]
    if response_header["status_code"] == 200: # All good, we can work with the response
        return get_first_lyrics_words(response_body["lyrics"]["lyrics_body"])
    else: # Something happened, return an error
        return "Error when looking up the song"


def parse_lyrics(lyrics):
    pass


def get_first_lyrics_words(s):
    s = s.replace("\n", " ").split(" ")
    s = list(filter(None, s))
    return s[:100]


found_id = search_song("somebody I used to know")
print(get_lyrics(track_id=found_id))
