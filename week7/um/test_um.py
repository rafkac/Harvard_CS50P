import pytest
from um import count


def test_um_basic():
    assert count("um") == 1


def test_um_with_comma():
    assert count("um,") == 1


def test_um_with_question_mark():
    assert count("um?") == 1


def test_um_case_insensitive():
    assert count("Um, thanks for the album.") == 1


def test_um_multiple():
    assert count("Um, thanks, um...") == 2


def test_um_not_substring():
    assert count("yummy") == 0


def test_um_empty_string():
    assert count("") == 0


def test_um_multiple_with_punctuation():
    assert count("um, um! um?") == 3
