import collections

from test_framework import generic_test
from test_framework.test_failure import PropertyName


DuplicateAndMissing = collections.namedtuple('DuplicateAndMissing', ('duplicate', 'missing'))


def find_duplicate_missing(A):
    x = A[0]
    y = 0
    for i in range(1, len(A)):
        x ^= A[i] ^ i

    set_bit = x & ~(x - 1)
    for i, num in enumerate(A):
        if i & set_bit:
            y ^= i
        if num & set_bit:
            y ^= num

    x ^= y
    if y in A:
        return DuplicateAndMissing(y, x)
    else:
        return DuplicateAndMissing(x, y)


def res_printer(prop, value):
    def fmt(x):
        return 'duplicate: {}, missing: {}'.format(x[0], x[1]) if x else None

    if prop in (PropertyName.EXPECTED, PropertyName.RESULT):
        return fmt(value)
    else:
        return value


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "search_for_missing_element.py",
            'find_missing_and_duplicate.tsv',
            find_duplicate_missing,
            res_printer=res_printer))
