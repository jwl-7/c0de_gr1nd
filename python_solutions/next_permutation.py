from test_framework import generic_test


def next_permutation(perm):
    i = len(perm) - 2
    while i >= 0 and perm[i] >= perm[i + 1]:
        i -= 1

    if i == -1:
        return []

    for j in reversed(range(i + 1, len(perm))):
        if perm[j] > perm[i]:
            perm[i], perm[j] = perm[j], perm[i]
            break

    perm[i + 1:len(perm) + 1] = perm[i + 1:len(perm) + 1][::-1]
    return perm


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "next_permutation.py", 'next_permutation.tsv', next_permutation))
