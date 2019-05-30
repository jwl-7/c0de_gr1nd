from test_framework import generic_test


def divide(x, y):
    quotient = 0
    while x >= y:
        y2 = y
        multiple = 1
        while x >= y2 << 1:
            multiple <<= 1
            y2 <<= 1
        quotient += multiple
        x -= y2
    return quotient


if __name__ == '__main__':
    exit(generic_test.generic_test_main("primitive_divide.py", "primitive_divide.tsv", divide))