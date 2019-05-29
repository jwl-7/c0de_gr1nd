from test_framework import generic_test


def closest_int_same_bit_count(x):
    for i in range(63):
        index_i = x >> i & 1
        index_j = x >> i + 1 & 1
        if index_i != index_j:
            x ^= 1 << i
            x ^= 1 << i + 1
            return x

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("closest_int_same_weight.py",
                                       "closest_int_same_weight.tsv",
                                       closest_int_same_bit_count))
