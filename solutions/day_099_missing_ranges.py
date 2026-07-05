def find_missing_ranges(nums, lower, upper):
    result = []
    prev = lower - 1
    for curr in nums + [upper + 1]:
        if curr - prev > 1:
            start = prev + 1
            end = curr - 1
            if start == end:
                result.append(str(start))
            else:
                result.append(f'{start}->{end}')
        prev = curr
    return result