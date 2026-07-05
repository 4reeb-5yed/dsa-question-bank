from solutions.day_087_non_overlapping_intervals import erase_overlap_intervals

def test_overlapping():
    assert erase_overlap_intervals([[1,2], [2,3], [3,4], [1,3]]) == 1

def test_no_overlap():
    assert erase_overlap_intervals([[1,2], [3,4]]) == 0

def test_all_overlap():
    assert erase_overlap_intervals([[1,2], [1,2], [1,2]]) == 2