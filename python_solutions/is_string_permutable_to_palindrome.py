import collections

from test_framework import generic_test


def can_form_palindrome(s):
    odd = 0
    for count in collections.Counter(s).values():
        if count % 2:
            odd += 1
    return odd <= 1


def can_form_palindrome_pythonic(s):
    return sum(count % 2 for count in collections.Counter(s).values()) <= 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "is_string_permutable_to_palindrome.py",
            'is_string_permutable_to_palindrome.tsv', can_form_palindrome))
