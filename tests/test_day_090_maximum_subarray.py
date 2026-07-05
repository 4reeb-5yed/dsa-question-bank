from solutions.day_090_maximum_subarray import max_sub_array

def test_basic():
    assert max_sub_array([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6

def test_all_negative():
    assert max_sub_array([-1]) == -1

def test_single_element():
    assert max_sub_array([5]) == 5