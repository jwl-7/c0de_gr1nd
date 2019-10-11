from test_framework import generic_test
from test_framework.test_failure import TestFailure


def decoding(s):
    decoded = ''
    count = ''
    for char in s:
        if char.isdigit():
            count += char
        else:
            decoded += int(count) * char
            count = ''
    return decoded


def encoding(s):
    encoded = ''
    prev = s[0]
    count = 0
    for char in s:
        if char == prev:
            count += 1
        else:
            encoded += str(count) + prev
            prev = char
            count = 1
    encoded += str(count) + char
    return encoded


def rle_tester(encoded, decoded):
    if decoding(encoded) != decoded:
        raise TestFailure('Decoding failed')
    if encoding(decoded) != encoded:
        raise TestFailure('Encoding failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("run_length_compression.py",
                                       'run_length_compression.tsv',
                                       rle_tester))
