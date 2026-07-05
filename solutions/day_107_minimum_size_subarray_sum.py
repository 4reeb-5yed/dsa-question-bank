def min_sub_array_len(s, nums):
    left = 0
    total = 0
    result = float('inf')
    for right in range(len(nums)):
        total += nums[right]
        while total >= s:
            result = min(result, right - left + 1)
            total -= nums[left]
            left += 1
    return result if result != float('inf') else 0