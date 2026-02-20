import pytest
from jar import Jar


def test_init():
    jar_1 = Jar()
    assert jar_1.capacity == 12
    assert jar_1.size == 0

    jar_2 = Jar(24)
    assert jar_2.capacity == 24
    assert jar_2.size == 0


def test_str():
    jar_empty = Jar()
    assert str(jar_empty) == ""
    jar = Jar()
    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪"


def test_deposit():
    jar_1 = Jar()
    jar_1.deposit(5)
    assert jar_1.size == 5

    jar_2 = Jar(7)
    jar_2.deposit(3)
    jar_2.deposit(4)
    assert jar_2.size == 7


def test_deposit_negative():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.deposit(-1)


def test_deposit_exceeds_capacity():
    jar = Jar(12)
    with pytest.raises(ValueError):
        jar.deposit(13)


def test_withdraw():
    jar_1 = Jar()
    jar_1.deposit(5)
    jar_1.withdraw(2)
    assert jar_1.size == 3

    jar_2 = Jar()
    jar_2.deposit(5)
    jar_2.withdraw(5)
    assert jar_2.size == 0


def test_withdraw_negative():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.withdraw(-1)


def test_withdraw_exceeds_size():
    jar = Jar()
    jar.deposit(3)
    with pytest.raises(ValueError):
        jar.withdraw(4)
