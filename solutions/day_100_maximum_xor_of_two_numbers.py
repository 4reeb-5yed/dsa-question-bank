def find_maximum_xor(nums):
    result = 0
    mask = 0
    for i in range(31, -1, -1):
        mask |= (1 << i)
        seen = set()
        for num in nums:
            seen.add(num & mask)
        candidate = result | (1 << i)
        for prefix in seen:
            if (prefix ^ candidate) in seen:
                result = candidate
                break
    return result