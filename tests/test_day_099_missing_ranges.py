from solutions.day_099_missing_ranges import find_missing_ranges

def test_basic():
    result = find_missing_ranges([2, 3, 5], 0, 5)
    assert '0->1' in result

def test_no_missing():
    assert find_missing_ranges([0, 1, 2, 3], 0, 3) == []

def test_edges():
    assert find_missing_ranges([], 1, 3) == ['1->3']