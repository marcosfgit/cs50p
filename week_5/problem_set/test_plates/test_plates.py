from plates import is_valid


def test_first_two_characters():
    assert is_valid("AA") == True
    assert is_valid("A2") == False


def test_two_to_six_characters():
    assert is_valid("AA") == True
    assert is_valid("AAAAAA") == True
    assert is_valid("A") == False
    assert is_valid("AAAAAAA") == False


def test_first_number_not_zero():
    assert is_valid("AAAAA1") == True
    assert is_valid("AA0") == False


def test_no_letters_after_number():
    assert is_valid("AAAA22") == True
    assert is_valid("AA22AA") == False


def test_no_periods_spaces_ponctuation():
    assert is_valid("AAA.22") == False
    assert is_valid("AAA 22") == False
    assert is_valid("AAA!22") == False
