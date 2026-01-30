from plates import is_valid

def test_no_numbers_first():
    assert is_valid("50CS") == False
    assert is_valid("100") == False

def test_numbers_last():
    assert is_valid("CS50") == True
    assert is_valid("MR200") == True

def test_length():
    assert is_valid("X") == False
    assert is_valid("ABC1234") == False

def no_starting_zero():
    assert is_valid("CS05") == False
    assert is_valid("X01") == False

def test_number():
    assert is_valid("CS50P") == False
    assert is_valid("AAA222") == True
    assert is_valid("AAA22A") == False
    assert is_valid("CS50X") == False

def test_other():
    assert is_valid("PI3.14") == False
    assert is_valid("HI,bro") == False

