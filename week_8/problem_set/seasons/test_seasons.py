from seasons import convert
from datetime import date, timedelta
import pytest


def test_format():
    one_year_ago = (date.today() - timedelta(days=365)).isoformat()
    assert convert(one_year_ago) == "Five hundred twenty-five thousand, six hundred minutes"
    two_years_ago = (date.today() - timedelta(days=730)).isoformat()
    assert convert(two_years_ago) == "One million, fifty-one thousand, two hundred minutes"

def test_invalid_date():
    with pytest.raises(SystemExit):
        convert("February 6th, 1998")
    with pytest.raises(SystemExit):
        convert("1999/01/01")
