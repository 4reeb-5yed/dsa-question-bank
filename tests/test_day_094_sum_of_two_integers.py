from solutions.day_094_sum_of_two_integers import get_sum

def test_basic():
    assert get_sum(1, 2) == 3
    assert get_sum(5, 7) == 12

def test_negative():
    assert get_sum(-1, 1) == 0
    assert get_sum(-5, 2) == -3

def test_zero():
    assert get_sum(0, 0) == 0
    assert get_sum(0, 5) == 5