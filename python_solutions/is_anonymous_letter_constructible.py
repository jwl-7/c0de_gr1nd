import collections

from test_framework import generic_test


def is_letter_constructible_from_magazine(letter_text, magazine_text):
    letter = collections.Counter(letter_text)
    for char in magazine_text:
        if char in letter:
            letter[char] -= 1
            if letter[char] == 0:
                del letter[char]
                if not letter:
                    return True
    return not letter


def is_letter_constructible_from_magazine_pythonic(letter_text, magazine_text):
    return not collections.Counter(letter_text) - collections.Counter(magazine_text)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_anonymous_letter_constructible.py",
                                       'is_anonymous_letter_constructible.tsv',
                                       is_letter_constructible_from_magazine))
