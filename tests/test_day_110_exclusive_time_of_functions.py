from solutions.day_110_exclusive_time_of_functions import exclusive_time

def test_basic():
    n = 2
    logs = ['0:start:0','1:start:2','1:end:5','0:end:6']
    assert exclusive_time(n, logs) == [3, 4]

def test_nested():
    n = 2
    logs = ['0:start:0','0:end:10']
    assert exclusive_time(n, logs) == [11, 0]

def test_multiple():
    n = 2
    logs = ['0:start:0','1:start:2','1:end:3','0:end:5']
    assert exclusive_time(n, logs) == [4, 2]