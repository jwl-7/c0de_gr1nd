from test_framework import generic_test


def test_collatz_conjecture(n):
    return n > 0


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("collatz_checker.py",
                                       'collatz_checker.tsv',
                                       test_collatz_conjecture))
