from solutions.day_104_132_pattern import find132pattern

def test_basic():
    assert find132pattern([1, 2, 3, 4]) == False
    assert find132pattern([3, 1, 4, 2]) == True

def test_negative():
    assert find132pattern([-1, 3, 2, 0]) == True