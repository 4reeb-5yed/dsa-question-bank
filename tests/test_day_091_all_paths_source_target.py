from solutions.day_091_all_paths_source_target import all_paths_source_target

def test_basic():
    graph = [[1,2], [3], [3], []]
    result = all_paths_source_target(graph)
    assert len(result) == 2
    assert [0, 1, 3] in result
    assert [0, 2, 3] in result

def test_single_path():
    graph = [[1], []]
    result = all_paths_source_target(graph)
    assert result == [[0, 1]]

def test_multiple_paths():
    graph = [[1,2,3], [2], [3], []]
    result = all_paths_source_target(graph)
    assert len(result) == 3