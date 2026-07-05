from solutions.day_106_bitwise_and_of_range import range_bitwise_and

def test_basic():
    assert range_bitwise_and(5, 7) == 4

def test_same():
    assert range_bitwise_and(1, 1) == 1

def test_large_range():
    assert range_bitwise_and(0, 0) == 0