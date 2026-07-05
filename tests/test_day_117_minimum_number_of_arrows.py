from solutions.day_117_minimum_number_of_arrows import find_min_arrows

def test_basic():
    assert find_min_arrows([[10,16],[2,8],[1,6],[7,12]]) == 2

def test_no_overlap():
    assert find_min_arrows([[1,2],[3,4],[5,6]]) == 3

def test_all_overlap():
    assert find_min_arrows([[1,2]]) == 1