from solutions.day_102_best_sightseeing_pair import max_score_sightseeing_pair

def test_basic():
    assert max_score_sightseeing_pair([8, 1, 5, 2, 6]) == 11

def test_two_elements():
    assert max_score_sightseeing_pair([1, 2]) == 2

def test_decreasing():
    assert max_score_sightseeing_pair([9, 4, 3, 2]) == 12