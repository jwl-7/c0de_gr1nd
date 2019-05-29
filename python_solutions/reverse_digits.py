from test_framework import generic_test


def reverse(x):
    if x < 0:
        x = str(abs(x))[::-1]
        x = -int(x)
        return x
    else:
        x = str(x)[::-1]
        return int(x)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("reverse_digits.py",
                                       'reverse_digits.tsv', reverse))
