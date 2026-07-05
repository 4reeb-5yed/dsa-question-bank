def insert_interval(intervals, new_interval):
    result = []
    i = 0
    n = len(intervals)
    while i < n and intervals[i][0] < new_interval[0]:
        result.append(intervals[i])
        i += 1
    if not result or result[-1][1] < new_interval[0]:
        result.append(new_interval)
    else:
        result[-1][1] = max(result[-1][1], new_interval[1])
    while i < n:
        if result[-1][1] < intervals[i][0]:
            result.append(intervals[i])
        else:
            result[-1][1] = max(result[-1][1], intervals[i][1])
        i += 1
    return result