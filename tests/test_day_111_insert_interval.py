from solutions.day_111_insert_interval import insert_interval

def test_basic():
    assert insert_interval([[1,3],[6,9]], [2,5]) == [[1,5],[6,9]]

def test_no_overlap():
    assert insert_interval([[1,2],[3,4]], [5,6]) == [[1,2],[3,4],[5,6]]

def test_merge_all():
    assert insert_interval([[1,5]], [0,10]) == [[0,10]]