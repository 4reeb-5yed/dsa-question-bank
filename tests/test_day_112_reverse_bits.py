from solutions.day_112_reverse_bits import reverse_bits

def test_basic():
    assert reverse_bits(43261596) == 964176192

def test_zero():
    assert reverse_bits(0) == 0

def test_max():
    assert reverse_bits(4294967295) == 4294967295