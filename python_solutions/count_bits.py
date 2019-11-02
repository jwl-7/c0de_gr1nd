from test_framework import generic_test


def count_bits(x):
    count = 0
    while x:
        count += x & 1
        x >>= 1
    return count


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("count_bits.py", 'count_bits.tsv',
                                       count_bits))
