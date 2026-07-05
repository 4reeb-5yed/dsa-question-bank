from solutions.day_098_validate_stack_sequences import validate_stack_sequences

def test_basic():
    assert validate_stack_sequences([1,2,3,4,5], [4,5,3,2,1]) == True

def test_not_valid():
    assert validate_stack_sequences([1,2,3,4,5], [4,3,5,1,2]) == False

def test_single_element():
    assert validate_stack_sequences([1], [1]) == True
    assert validate_stack_sequences([1], [2]) == False