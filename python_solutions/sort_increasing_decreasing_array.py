import heapq

from test_framework import generic_test


def sort_k_increasing_decreasing_array(A):
    sub_arrays = []
    increasing = True
    start = 0
    for i in range(1, len(A)):
        if A[i] >= A[i-1] and not increasing:
            sub_arrays.append(A[i-1:start-1:-1])
            increasing = True
            start = i
        elif A[i] < A[i-1] and increasing:
            sub_arrays.append(A[start:i])
            increasing = False
            start = i
        if i == len(A) - 1:
            if not increasing:
                sub_arrays.append(A[:start-1:-1])
            else:
                sub_arrays.append(A[start:])
    return list(heapq.merge(*sub_arrays))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sort_increasing_decreasing_array.py",
                                       'sort_increasing_decreasing_array.tsv',
                                       sort_k_increasing_decreasing_array))
