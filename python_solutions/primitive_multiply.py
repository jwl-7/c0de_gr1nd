from test_framework import generic_test


def add(x, y):
    while y != 0:
        carry = x & y
        x ^= y
        y = carry << 1
    return x

def multiply(x, y):
    product = 0
    while y != 0:
        if y & 1:
            product = add(product, x)
        x <<= 1
        y >>= 1
    return product


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("primitive_multiply.py",
                                       'primitive_multiply.tsv', multiply))
