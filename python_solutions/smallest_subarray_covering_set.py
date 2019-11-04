import collections
import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


Subarray = collections.namedtuple('Subarray', ('start', 'end'))


def find_smallest_subarray_covering_set(paragraph, keywords):
    need = collections.Counter(keywords)
    missing = len(keywords)
    start, end = 0, 0
    i = 0
    for j, s in enumerate(paragraph):
        missing -= need[s] > 0
        need[s] -= 1
        if not missing:
            while need[paragraph[i]] < 0:
                need[paragraph[i]] += 1
                i += 1
            if not end or j - i < end - start:
                start, end = i, j
            need[paragraph[i]] += 1
            missing += 1
            i += 1
    return Subarray(start, end)


@enable_executor_hook
def find_smallest_subarray_covering_set_wrapper(executor, paragraph, keywords):
    copy = keywords

    (start, end) = executor.run(
        functools.partial(find_smallest_subarray_covering_set, paragraph,
                          keywords))

    if (start < 0 or start >= len(paragraph) or end < 0
            or end >= len(paragraph) or start > end):
        raise TestFailure("Index out of range")

    for i in range(start, end + 1):
        copy.discard(paragraph[i])

    if copy:
        raise TestFailure("Not all keywords are in the range")

    return end - start + 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "smallest_subarray_covering_set.py",
            "smallest_subarray_covering_set.tsv",
            find_smallest_subarray_covering_set_wrapper))
