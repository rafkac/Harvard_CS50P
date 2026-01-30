import pytest
from fuel import convert, gauge


def test_fractions():
    assert convert("3/4") == 75
    assert convert("1/4") == 25


def test_exceptions():
    with pytest.raises(ValueError):
        convert("cat/dog")
    with pytest.raises(ZeroDivisionError):
        convert("4/0")
    with pytest.raises(ValueError):
        convert("2/1")


def test_negative():
    with pytest.raises(ValueError):
        convert("-1/2")


def test_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(100) == "F"
    assert gauge(99) == "F"
    assert gauge(50) == "50%"
    assert gauge(23) == "23%"

