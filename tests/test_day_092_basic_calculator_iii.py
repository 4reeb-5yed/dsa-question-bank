from solutions.day_092_basic_calculator_iii import calculate

def test_basic_add_sub():
    assert calculate('1 + 1') == 2
    assert calculate('2 - 1') == 1

def test_mult_div():
    assert calculate('2 * 3') == 6
    assert calculate('8 / 4') == 2

def test_complex():
    assert calculate('1 + 2 * 3') == 7
    assert calculate('(2 + 3) * 4') == 20