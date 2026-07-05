def get_sum(a, b):
    while b != 0:
        carry = (a & b) << 1
        a = a ^ b
        b = carry & 0xFFFFFFFF
        if b != 0:
            a = a & 0xFFFFFFFF
    return a if a <= 0x7FFFFFFF else a - 0x100000000