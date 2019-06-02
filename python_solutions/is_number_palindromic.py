from test_framework import generic_test


def is_palindrome_number(x):
    if x < 0:
        return False
    reverse = str(x)[::-1]
    if x == int(reverse):
        return True
    else:
        return False


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_number_palindromic.py",
                                       "is_number_palindromic.tsv",
                                       is_palindrome_number))