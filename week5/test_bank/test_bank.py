from bank import value

def test_hello():
    assert value("Hello David") == 0
    assert value("Hello, Max") == 0

def test_h():
    assert value("Hi David") == 20
    assert value("hey, Max") == 20

def test_100():
    assert value("Yo man") == 100
    assert value("Wagwan") == 100
