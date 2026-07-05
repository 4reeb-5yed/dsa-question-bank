from solutions.day_086_stack_of_plates import SetOfStacks

def test_push_and_pop():
    s = SetOfStacks(3)
    s.push(1); s.push(2); s.push(3); s.push(4)
    assert s.pop() == 4
    assert s.pop() == 3

def test_pop_at():
    s = SetOfStacks(2)
    s.push(1); s.push(2); s.push(3); s.push(4)
    assert s.pop_at(0) == 2
    assert s.pop_at(0) == 1

def test_multiple_stacks():
    s = SetOfStacks(2)
    for i in range(1, 7):
        s.push(i)
    assert s.stacks == [[1, 2], [3, 4], [5, 6]]