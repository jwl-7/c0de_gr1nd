from test_framework import generic_test
from sortedcontainers import SortedDict


def find_closest_elements_in_sorted_arrays(sorted_arrays):
    diff = float('inf')
    tree = SortedDict()
    for idx, array in enumerate(sorted_arrays):
        i = iter(array)
        nxt = next(i)
        tree[(nxt, idx)] = i
    while True:
        min_val, min_idx = tree.peekitem(0)[0]
        max_val = tree.peekitem()[0][0]
        diff = min(diff, max_val - min_val)
        i = tree.popitem(0)[1]
        nxt = next(i, None)
        if nxt is None:
            return diff
        tree[(nxt, min_idx)] = i


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("minimum_distance_3_sorted_arrays.py",
                                       'minimum_distance_3_sorted_arrays.tsv',
                                       find_closest_elements_in_sorted_arrays))
