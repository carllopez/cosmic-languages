from .fixtures import TRACK_LYRICS, TRACK_RESPONSE

import json
from requests.models import Response

from lyrics.client import LyricsClient


def test_find_track(mocker):
    response = Response()
    response.status_code = 200
    response.json = mocker.Mock(return_value=json.loads(TRACK_RESPONSE))
    mocker.patch("lyrics.client.LyricsClient.get", return_value=response)

    client = LyricsClient(key="TESTKEY")
    resp = client.search_song(title="Testing song finder")

    # Proper track id returned
    assert resp == 180838062


def test_get_lyrics(mocker):
    response = Response()
    response.status_code = 200
    response.json = mocker.Mock(return_value=json.loads(TRACK_LYRICS))
    mocker.patch("lyrics.client.LyricsClient.get", return_value=response)

    client = LyricsClient(key="TESTKEY")

    track_id = 180838062
    response = client.get_lyrics(track_id=track_id)

    assert isinstance(response, list)
    assert len(response) == 100
