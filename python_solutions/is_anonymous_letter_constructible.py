import collections

from test_framework import generic_test


def is_letter_constructible_from_magazine(letter_text, magazine_text):
    letter = collections.Counter(letter_text)
    magazine = collections.Counter(magazine_text)
    for char in letter:
        if char not in magazine.keys() or letter[char] > magazine[char]:
            return False
    return True


def is_letter_constructible_from_magazine_pythonic(letter_text, magazine_text):
    return not collections.Counter(letter_text) - collections.Counter(magazine_text)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_anonymous_letter_constructible.py",
                                       'is_anonymous_letter_constructible.tsv',
                                       is_letter_constructible_from_magazine))
