from solutions.day_103_shortest_distance_from_all_buildings import shortest_distance

def test_basic():
    grid = [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]
    assert shortest_distance(grid) == 7

def test_no_reachable():
    grid = [[1,0],[0,1]]
    assert shortest_distance(grid) == 2