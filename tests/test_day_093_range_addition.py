from solutions.day_093_range_addition import get_modified_array

def test_basic():
    assert get_modified_array(5, [[1, 3, 2], [2, 4, 3]]) == [0, 2, 5, 5, 3]

def test_single_element():
    assert get_modified_array(1, [[0, 0, 5]]) == [5]

def test_no_updates():
    assert get_modified_array(3, []) == [0, 0, 0]