from twttr import shorten


def test_word():
    assert shorten("hello") == "hll"


def test_capitalized_word():
    assert shorten("HELLO") == "HLL"


def test_numbers():
    assert shorten("CS50") == "CS50"


def test_ponctuation():
    assert shorten("CS50!") == "CS50!"
