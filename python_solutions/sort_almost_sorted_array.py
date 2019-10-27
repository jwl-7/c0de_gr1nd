import heapq
import itertools

from test_framework import generic_test


def sort_approximately_sorted_array(sequence, k):
    min_heap = []
    result = []
    for i in itertools.islice(sequence, k):
        heapq.heappush(min_heap, i)
    for i in sequence:
        result.append(heapq.heappushpop(min_heap, i))
    while min_heap:
        result.append(heapq.heappop(min_heap))
    return result


def sort_approximately_sorted_array_wrapper(sequence, k):
    return sort_approximately_sorted_array(iter(sequence), k)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "sort_almost_sorted_array.py", 'sort_almost_sorted_array.tsv',
            sort_approximately_sorted_array_wrapper))
