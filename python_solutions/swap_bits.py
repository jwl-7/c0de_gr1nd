from test_framework import generic_test


def swap_bits(x, i, j):
    index_i = x >> i & 1
    index_j = x >> j & 1
    if index_i != index_j:
        x ^= 1 << i
        x ^= 1 << j
    return x


if __name__ == '__main__':
    exit(generic_test.generic_test_main("swap_bits.py", 'swap_bits.tsv', swap_bits))