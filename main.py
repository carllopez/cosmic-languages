import json
import requests

from dictionary.client import DictionaryClient
from lyrics.client import LyricsClient

# MusixMatch API key
MUSIXMATCH_KEY = "b0be994f81a9800e914305c52f237eef"

# Init APIs clients
lyrics_client = LyricsClient(key=MUSIXMATCH_KEY)
dictionary_client = DictionaryClient()

# Get song id with title
found_id = lyrics_client.search_song("blackened")
# Get lyrics with song id
lyrics_as_words = lyrics_client.get_lyrics(track_id=found_id)

# Look up all words in lyrics
dictionary_results = {}
for word in lyrics_as_words:
    result = dictionary_client.lookup_word(word)
    # None will be stored if the word couldn't be found or if
    # we tried to lookup a symbol eg. "********"
    dictionary_results[word] = result if not isinstance(result, str) else None

print(dictionary_results)
