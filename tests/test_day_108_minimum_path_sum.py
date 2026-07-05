from solutions.day_108_minimum_path_sum import min_path_sum

def test_basic():
    assert min_path_sum([[1,3,1],[1,5,1],[4,2,1]]) == 7

def test_single_element():
    assert min_path_sum([[5]]) == 5

def test_two_by_two():
    assert min_path_sum([[1,2],[1,1]]) == 3