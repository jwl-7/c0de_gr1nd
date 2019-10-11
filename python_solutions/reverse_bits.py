from test_framework import generic_test


def reverse_bits(x):
    j = 63
    for i in range(32):
        lsb = x >> i & 1
        msb = x >> j & 1
        if lsb != msb:
            x ^= 1 << i
            x ^= 1 << j
        j -= 1
    return x


def reverse_bits_pythonic(x):
    return int(bin(x)[2:].zfill(64)[::-1], 2)


if __name__ == '__main__':
    exit(generic_test.generic_test_main("reverse_bits.py", "reverse_bits.tsv", reverse_bits))
