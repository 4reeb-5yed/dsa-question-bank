from solutions.day_097_graph_valid_tree import valid_tree

def test_valid_tree():
    assert valid_tree(5, [[0,1], [0,2], [0,3], [1,4]]) == True

def test_not_connected():
    assert valid_tree(5, [[0,1], [2,3]]) == False

def test_cycle():
    assert valid_tree(4, [[0,1], [1,2], [2,0]]) == False