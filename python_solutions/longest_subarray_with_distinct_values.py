from test_framework import generic_test


def longest_subarray_with_distinct_entries(A):
    recent = {}
    result = 0
    start = 0
    for i, s in enumerate(A):
        if s not in recent or recent[s] < start:
            result = max(result, i - start + 1)
        else:
            start = recent[s] + 1
        recent[s] = i
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "longest_subarray_with_distinct_values.py",
            'longest_subarray_with_distinct_values.tsv',
            longest_subarray_with_distinct_entries))
