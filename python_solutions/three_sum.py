from test_framework import generic_test


def has_two_sum(A, t):
    i = 0
    j = len(A) - 1
    while i <= j:
        if A[i] + A[j] == t:
            return True
        elif A[i] + A[j] < t:
            i += 1
        else:
            j -= 1
    return False


def has_three_sum(A, t):
    A.sort()
    return any(has_two_sum(A, t - x) for x in A)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("three_sum.py", "three_sum.tsv",
                                       has_three_sum))
