from solutions.day_120_triangle_minimum_path import minimum_total

def test_basic():
    triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
    assert minimum_total(triangle) == 11

def test_single():
    assert minimum_total([[2]]) == 2

def test_two_rows():
    triangle = [[2],[3,4]]
    assert minimum_total(triangle) == 5