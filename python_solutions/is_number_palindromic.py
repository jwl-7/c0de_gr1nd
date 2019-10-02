from test_framework import generic_test


def is_palindrome_number(x):
    if x < 0:
        return False
    reverse = 0
    tmp = x
    while tmp:
        reverse = reverse * 10 + tmp % 10
        tmp //= 10
    return x == reverse


def is_palindrome_number_pythonic(x):
    return False if x < 0 else x == int(str(x)[::-1])


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_number_palindromic.py",
                                       "is_number_palindromic.tsv",
                                       is_palindrome_number))