from solutions.day_101_find_all_anagrams import find_anagrams

def test_basic():
    assert find_anagrams('cbaebabacd', 'abc') == [0, 6]

def test_no_anagrams():
    assert find_anagrams('hello', 'xyz') == []

def test_multiple():
    assert 2 in find_anagrams('abab', 'ab')