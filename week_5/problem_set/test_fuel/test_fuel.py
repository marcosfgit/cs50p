from fuel import convert, gauge
import pytest

def test_percentage():
    assert convert("1/4") == 25


def test_zero_division_error():
    with pytest.raises(ZeroDivisionError):
        convert("4/0")


def test_value_error():
    with pytest.raises(ValueError):
        convert("5/4")
    with pytest.raises(ValueError):
        convert("-1/4")


def test_gauge():
    assert gauge(25) == "25%"
    assert gauge(1) == "E"
    assert gauge(99) == "F"
