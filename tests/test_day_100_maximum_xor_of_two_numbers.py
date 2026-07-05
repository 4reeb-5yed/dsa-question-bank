from solutions.day_100_maximum_xor_of_two_numbers import find_maximum_xor

def test_basic():
    assert find_maximum_xor([3, 10, 5, 25, 2, 8]) == 28

def test_two_elements():
    assert find_maximum_xor([0, 2]) == 2

def test_same_elements():
    assert find_maximum_xor([5, 5, 5]) == 0