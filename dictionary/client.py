import requests


# Dictionary API
DICTIONARY_BASE_URL = "https://api.dictionaryapi.dev/api/v2/entries/en_US/"


class DictionaryClient(object):

    def __init__(self):
        self.base_url = DICTIONARY_BASE_URL

    def get(self, word, payload={}):
        if not word:
            return None

        response = requests.get(f"{self.base_url}{word}", params=payload)
        return response

    def lookup_word(self, word):
        response = self.get(word=word)

        formatted_response = response.json()

        if response.status_code == 200: # All good, we can work with the response
            return formatted_response[0]
        else: # Something happened, return an error
            return "Error when looking up the word"
