from test_framework import generic_test


def apply_permutation(perm, A):
    B = [0] * len(A)
    for i in range(len(A)):
        B[perm[i]] = A[i]
    A[:] = B


def apply_permutation_wrapper(perm, A):
    apply_permutation(perm, A)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("apply_permutation.py",
                                       "apply_permutation.tsv",
                                       apply_permutation_wrapper))
