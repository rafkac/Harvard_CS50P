from twttr import shorten


def test_shorten():
    assert shorten("Twitter") == "Twttr"


def test_capitalized():
    assert shorten("OMG") == "MG"


def test_numbers():
    assert shorten("Test123") == "Tst123"


def test_punctuation():
    assert shorten("String, and some other string.") == "Strng, nd sm thr strng."
