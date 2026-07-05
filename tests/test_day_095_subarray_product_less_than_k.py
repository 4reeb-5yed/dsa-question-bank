from solutions.day_095_subarray_product_less_than_k import num_subarray_product_less_than_k

def test_basic():
    assert num_subarray_product_less_than_k([10, 5, 2, 6], 100) == 8

def test_k_too_small():
    assert num_subarray_product_less_than_k([1, 2, 3], 1) == 0

def test_all_valid():
    assert num_subarray_product_less_than_k([1, 1, 1], 2) == 6