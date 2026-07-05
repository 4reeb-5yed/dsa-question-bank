import heapq

def smallest_range(nums):
    heap = []
    current_max = float('-inf')
    for i, arr in enumerate(nums):
        heapq.heappush(heap, (arr[0], i, 0))
        current_max = max(current_max, arr[0])
    range_start, range_end = float('-inf'), float('inf')
    while True:
        min_val, list_idx, elem_idx = heap[0]
        if current_max - min_val < range_end - range_start:
            range_start, range_end = min_val, current_max
        if elem_idx + 1 == len(nums[list_idx]):
            break
        next_val = nums[list_idx][elem_idx + 1]
        heapq.heapreplace(heap, (next_val, list_idx, elem_idx + 1))
        current_max = max(current_max, next_val)
    return [range_start, range_end]