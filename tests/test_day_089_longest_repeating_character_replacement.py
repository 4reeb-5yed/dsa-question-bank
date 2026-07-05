from solutions.day_089_longest_repeating_character_replacement import character_replacement

def test_basic():
    assert character_replacement('ABAB', 2) == 4

def test_no_replacement():
    assert character_replacement('AABABBA', 1) == 4

def test_all_same():
    assert character_replacement('AAAA', 0) == 4