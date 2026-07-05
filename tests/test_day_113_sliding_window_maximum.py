from solutions.day_113_sliding_window_maximum import max_sliding_window

def test_basic():
    assert max_sliding_window([1,3,-1,-3,5,3,6,7], 3) == [3,3,5,5,6,7]

def test_single():
    assert max_sliding_window([1], 1) == [1]

def test_decreasing():
    assert max_sliding_window([9,8,7,6,5,4,3,2,1], 3) == [9,8,7,6,5,4,3]