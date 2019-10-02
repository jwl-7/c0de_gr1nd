from test_framework import generic_test


def reverse(x):
    r = 0
    tmp = abs(x)
    while tmp:
        r = r * 10 + tmp % 10
        tmp //= 10
    return -r if x < 0 else r


def reverse_pythonic(x):
    return -int(str(abs(x))[::-1]) if x < 0 else int(str(x)[::-1])


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("reverse_digits.py",
                                       'reverse_digits.tsv', reverse))