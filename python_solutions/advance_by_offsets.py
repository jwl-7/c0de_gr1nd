from test_framework import generic_test


def can_reach_end(A):
    furthest = 0
    end = len(A) - 1
    i = 0
    while i <= furthest and furthest < end:
        furthest = max(furthest, A[i] + i)
        i += 1
    return furthest >= end


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "advance_by_offsets.py", "advance_by_offsets.tsv", can_reach_end))