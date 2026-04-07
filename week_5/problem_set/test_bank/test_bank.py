from bank import value


def test_hello():
    assert value("hello") == 0


def test_word_starting_h():
    assert value("hey") == 20


def test_word_not_starting_h():
    assert value("greetings") == 100


def test_capitalized_word():
    assert value("HELLO") == 0


def test_multiple_worlds():
    assert value("hello my dear friend") == 0
