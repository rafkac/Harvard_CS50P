import pytest
from numb3rs import validate

def test_valid_ipv4():
    assert validate("192.168.1.1") == True
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True
    assert validate("127.0.0.1") == True


def test_invalid_ipv4_out_of_range():
    assert validate("256.1.1.1") == False
    assert validate("1.256.1.1") == False
    assert validate("1.1.256.1") == False
    assert validate("1.1.1.256") == False
    assert validate("999.999.999.999") == False


def test_invalid_ipv4_leading_zeros():
    assert validate("01.1.1.1") == False
    assert validate("1.01.1.1") == False
    assert validate("1.1.01.1") == False
    assert validate("1.1.1.01") == False


def test_invalid_ipv4_format():
    assert validate("1.1.1") == False
    assert validate("1.1.1.1.1") == False
    assert validate("a.b.c.d") == False
    assert validate("1.1.1.a") == False
    assert validate("...") == False
    assert validate("") == False
    assert validate("cat") == False


def test_invalid_ipv4_missing_octets():
    assert validate(".1.1.1") == False
    assert validate("1..1.1") == False
    assert validate("1.1.1.") == False

