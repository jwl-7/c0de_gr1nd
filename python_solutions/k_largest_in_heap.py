import heapq

from test_framework import generic_test, test_utils


def k_largest_in_binary_heap(A, k):
    if k <= 0:
        return []

    max_heap = []
    result = []
    max_heap.append((-A[0], 0))

    for _ in range(k):
        largest_idx = max_heap[0][1]
        result.append(-heapq.heappop(max_heap)[0])

        left = 2 * largest_idx + 1
        if left < len(A):
            heapq.heappush(max_heap, (-A[left], left))

        right = 2 * largest_idx + 2
        if right < len(A):
            heapq.heappush(max_heap, (-A[right], right))
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "k_largest_in_heap.py",
            "k_largest_in_heap.tsv",
            k_largest_in_binary_heap,
            comparator=test_utils.unordered_compare))
