from solutions.day_105_meeting_rooms_ii import min_meeting_rooms

def test_basic():
    assert min_meeting_rooms([[0, 30], [5, 10], [15, 20]]) == 2

def test_no_overlap():
    assert min_meeting_rooms([[7, 10], [2, 4]]) == 1

def test_all_overlap():
    assert min_meeting_rooms([[1, 5], [2, 6], [3, 7]]) == 3