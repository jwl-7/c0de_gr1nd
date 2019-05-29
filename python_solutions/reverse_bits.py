from test_framework import generic_test


def reverse_bits(x):
    return int(bin(x)[2:].zfill(64)[::-1], 2)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("reverse_bits.py", "reverse_bits.tsv",
                                       reverse_bits))
