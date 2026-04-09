from numb3rs import validate


def test_format():
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True


def test_range():
    assert validate("275.3.6.28") == False
    assert validate("255.300.6.28") == False
    assert validate("255.3.600.28") == False
    assert validate("255.3.6.280") == False


def test_length():
    assert validate("10") == False
    assert validate("10.10") == False
    assert validate("10.10.10") == False
    assert validate("010.10.10.10") == False


def test_non_numeric():
    assert validate("cat") == False
