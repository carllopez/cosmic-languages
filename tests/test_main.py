from ..main import get_lyrics


def test_get_lyrics():
    title = "Imagine"
    response = get_lyrics(title=title)
    assert isinstance(response, str)
