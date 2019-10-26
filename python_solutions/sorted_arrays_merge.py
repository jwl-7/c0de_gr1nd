import heapq

from test_framework import generic_test


def merge_sorted_arrays(sorted_arrays):
    min_heap = []
    result = []
    for i in range(len(sorted_arrays)):
        heapq.heappush(min_heap, (sorted_arrays[i][0], i, 0))
    while min_heap:
        item, arr_idx, item_idx = heapq.heappop(min_heap)
        result.append(item)
        if item_idx + 1 < len(sorted_arrays[arr_idx]):
            item_idx += 1
            heapq.heappush(min_heap, (sorted_arrays[arr_idx][item_idx], arr_idx, item_idx))
    return result


def merge_sorted_arrays_pythonic(sorted_arrays):
    return list(heapq.merge(*sorted_arrays))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sorted_arrays_merge.py",
                                       "sorted_arrays_merge.tsv",
                                       merge_sorted_arrays))
