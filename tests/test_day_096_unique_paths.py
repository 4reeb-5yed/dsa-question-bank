from solutions.day_096_unique_paths import unique_paths

def test_basic():
    assert unique_paths(3, 7) == 28
    assert unique_paths(3, 2) == 3

def test_single_row_or_col():
    assert unique_paths(1, 1) == 1
    assert unique_paths(1, 10) == 1

def test_square():
    assert unique_paths(3, 3) == 6