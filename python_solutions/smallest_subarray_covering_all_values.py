import collections
import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


Subarray = collections.namedtuple('Subarray', ('start', 'end'))


def find_smallest_sequentially_covering_subset(paragraph, keywords):
    key_lookup = {}
    for i, s in enumerate(keywords):
        key_lookup[s] = i
    recent = [-1] * len(keywords)
    smallest = [float('inf')] * len(keywords)
    shortest = float('inf')
    start, end = 0, 0

    for i, s in enumerate(paragraph):
        if s in key_lookup:
            key_idx = key_lookup[s]
            if key_idx == 0:
                smallest[key_idx] = 1
            elif smallest[key_idx - 1] != float('inf'):
                prev_dist = i - recent[key_idx - 1]
                smallest[key_idx] = prev_dist + smallest[key_idx - 1]
            recent[key_idx] = i
            if key_idx == len(keywords) - 1 and smallest[-1] < shortest:
                shortest = smallest[-1]
                start, end = i - shortest + 1, i
    return Subarray(start, end)


@enable_executor_hook
def find_smallest_sequentially_covering_subset_wrapper(executor, paragraph,
                                                       keywords):
    result = executor.run(
        functools.partial(find_smallest_sequentially_covering_subset,
                          paragraph, keywords))

    kw_idx = 0
    para_idx = result.start
    if para_idx < 0:
        raise RuntimeError('Subarray start index is negative')

    while kw_idx < len(keywords):
        if para_idx >= len(paragraph):
            raise TestFailure("Not all keywords are in the generated subarray")
        if para_idx >= len(paragraph):
            raise TestFailure("Subarray end index exceeds array size")
        if paragraph[para_idx] == keywords[kw_idx]:
            kw_idx += 1
        para_idx += 1

    return result.end - result.start + 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "smallest_subarray_covering_all_values.py",
            'smallest_subarray_covering_all_values.tsv',
            find_smallest_sequentially_covering_subset_wrapper))
