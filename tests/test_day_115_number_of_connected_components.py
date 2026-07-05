from solutions.day_115_number_of_connected_components import count_components

def test_basic():
    assert count_components(5, [[0,1],[1,2],[3,4]]) == 2

def test_all_connected():
    assert count_components(4, [[0,1],[1,2],[2,3]]) == 1

def test_no_edges():
    assert count_components(3, []) == 3