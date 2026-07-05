from solutions.day_088_single_number_ii import single_number

def test_single_basic():
    assert single_number([2, 2, 3, 2]) == 3

def test_single_larger():
    assert single_number([0, 1, 0, 1, 0, 1, 99]) == 99

def test_single_negative():
    assert single_number([-2, -2, -2, -1]) == -1