from test_framework import generic_test


def reverse(x):
    if x < 0:
        return -int(str(abs(x))[::-1])
    else:
        return int(str(x)[::-1])


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("reverse_digits.py",
                                       'reverse_digits.tsv', reverse))