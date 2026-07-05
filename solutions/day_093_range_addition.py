def get_modified_array(length, updates):
    result = [0] * (length + 1)
    for start, end, val in updates:
        result[start] += val
        result[end + 1] -= val
    for i in range(1, length):
        result[i] += result[i - 1]
    return result[:-1]