from test_framework import generic_test


def longest_contained_range(A):
    A = set(A)
    longest = 0
    for x in A:
        if x - 1 not in A:
            y = x + 1
            while y in A:
                y += 1
            longest = max(longest, y - x)
    return longest


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("longest_contained_interval.py",
                                       'longest_contained_interval.tsv',
                                       longest_contained_range))
