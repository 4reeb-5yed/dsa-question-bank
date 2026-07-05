from solutions.day_118_count_bits import count_bits

def test_basic():
    assert count_bits(2) == [0, 1, 1]

def test_five():
    result = count_bits(5)
    assert result == [0, 1, 1, 2, 1, 2]

def test_zero():
    assert count_bits(0) == [0]