from solutions.day_116_simplify_path import simplify_path

def test_basic():
    assert simplify_path('/home/') == '/home'

def test_parent():
    assert simplify_path('/home/Downloads/../Pictures') == '/home/Pictures'

def test_double_slash():
    assert simplify_path('/a//b/c') == '/a/b/c'