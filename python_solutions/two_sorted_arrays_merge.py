from test_framework import generic_test


def merge_two_sorted_arrays(A, m, B, n):
    while m > 0 and n > 0:
        if A[m-1] > B[n-1]:
            A[m+n-1] = A[m-1]
            m -= 1
        else:
            A[m+n-1] = B[n-1]
            n -= 1
    while n > 0:
        A[m+n-1] = B[n-1]
        n -= 1


def merge_two_sorted_arrays_pythonic(A, m, B, n):
    A[m:] = B
    A.sort()


def merge_two_sorted_arrays_wrapper(A, m, B, n):
    merge_two_sorted_arrays_pythonic(A, m, B, n)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("two_sorted_arrays_merge.py",
                                       'two_sorted_arrays_merge.tsv',
                                       merge_two_sorted_arrays_wrapper))
