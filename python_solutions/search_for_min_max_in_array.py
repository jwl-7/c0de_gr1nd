import collections

from test_framework import generic_test
from test_framework.test_failure import PropertyName


MinMax = collections.namedtuple('MinMax', ('smallest', 'largest'))


def find_min_max(A):
    if len(A) % 2 == 0:
        minimum = min(A[0], A[1])
        maximum = max(A[0], A[1])
        i = 2
    else:
        minimum = maximum = A[0]
        i = 1
    while i < len(A) - 1:
        if A[i] < A[i+1]:
            minimum = min(minimum, A[i])
            maximum = max(maximum, A[i+1])
        else:
            minimum = min(minimum, A[i+1])
            maximum = max(maximum, A[i])
        i += 2
    return MinMax(minimum, maximum)


def res_printer(prop, value):
    def fmt(x):
        return 'min: {}, max: {}'.format(x[0], x[1]) if x else None

    if prop in (PropertyName.EXPECTED, PropertyName.RESULT):
        return fmt(value)
    else:
        return value


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "search_for_min_max_in_array.py",
            'search_for_min_max_in_array.tsv',
            find_min_max,
            res_printer=res_printer))
