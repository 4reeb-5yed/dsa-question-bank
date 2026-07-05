from solutions.day_119_smallest_range_covering_elements import smallest_range

def test_basic():
    nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
    result = smallest_range(nums)
    assert result[1] - result[0] == 20 or result == [20, 24]

def test_two_lists():
    nums = [[1,2,3],[1,2,3]]
    result = smallest_range(nums)
    assert result == [1, 1]