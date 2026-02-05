import pytest
from seasons import get_date, minutes_str
from datetime import date, timedelta


def test_get_date_valid():
    assert get_date("2000-01-01") == date(2000, 1, 1)
    assert get_date("2020-09-11") == date(2020, 9, 11)
    assert get_date("2016-02-29") == date(2016, 2, 29)


def test_get_date_invalid_format():
    with pytest.raises(ValueError):
        get_date("01/01/2000")
    with pytest.raises(ValueError):
        get_date("February 6th, 1998")
    with pytest.raises(ValueError):
        get_date("00-01-01")


def test_get_date_invalid_format_no_dashes():
    with pytest.raises(ValueError):
        get_date("20000101")


def test_get_date_invalid_month():
    with pytest.raises(ValueError):
        get_date("2000-13-01")


def test_get_date_invalid_day():
    with pytest.raises(ValueError):
        get_date("2000-04-31")
    with pytest.raises(ValueError):
        get_date("2001-02-29")


def test_minutes_str():
    # year ago (no leap year)
    year_ago = date.today() - timedelta(days=365)
    assert minutes_str(year_ago) == "Five hundred twenty-five thousand, six hundred minutes"
    two_years_ago = date.today() - timedelta(days=365*2)
    assert minutes_str(two_years_ago) == "One million, fifty-one thousand, two hundred minutes"


def test_get_date_non_leap_year():
    with pytest.raises(ValueError):
        get_date("2001-02-29")
