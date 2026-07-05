from solutions.day_107_minimum_size_subarray_sum import min_sub_array_len

def test_basic():
    assert min_sub_array_len(7, [2, 3, 1, 2, 4, 3]) == 2

def test_not_possible():
    assert min_sub_array_len(15, [1, 2, 3, 4, 5]) == 5

def test_single_element():
    assert min_sub_array_len(3, [1, 1]) == 0