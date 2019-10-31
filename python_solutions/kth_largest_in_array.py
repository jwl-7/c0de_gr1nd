import random

from test_framework import generic_test


# The numbering starts from one, i.e., if A = [3, 1, -1, 2]
# find_kth_largest(1, A) returns 3, find_kth_largest(2, A) returns 2,
# find_kth_largest(3, A) returns 1, and find_kth_largest(4, A) returns -1.
def find_kth_largest(k, A):
    left = 0
    right = len(A) - 1
    while left <= right:
        pivot = partition(A, left, right)
        if pivot == k - 1:
            return A[pivot]
        elif pivot < k - 1:
            left = pivot + 1
        else:
            right = pivot - 1


def partition(A, left, right):
    pivot_idx = random.randint(left, right)
    pivot_val = A[pivot_idx]
    new_pivot = left
    A[pivot_idx], A[right] = A[right], A[pivot_idx]
    for i in range(left, right):
        if A[i] > pivot_val:
            A[i], A[new_pivot] = A[new_pivot], A[i]
            new_pivot += 1
    A[right], A[new_pivot] = A[new_pivot], A[right]
    return new_pivot


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("kth_largest_in_array.py",
                                       'kth_largest_in_array.tsv',
                                       find_kth_largest))
