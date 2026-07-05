from solutions.day_109_01_matrix import update_matrix

def test_basic():
    mat = [[0,0,0],[0,1,0],[1,1,1]]
    result = update_matrix(mat)
    assert result[0][0] == 0
    assert result[1][2] == 0

def test_all_zeros():
    mat = [[0,0],[0,0]]
    result = update_matrix(mat)
    assert result == [[0,0],[0,0]]

def test_all_ones():
    mat = [[1,1],[1,1]]
    result = update_matrix(mat)
    assert result[0][0] == -1