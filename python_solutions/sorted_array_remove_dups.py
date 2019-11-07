import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def delete_duplicates(A):
    idx = 1
    for x in A[1:]:
        if x != A[idx-1]:
            A[idx] = x
            idx += 1
    return idx


@enable_executor_hook
def delete_duplicates_wrapper(executor, A):
    idx = executor.run(functools.partial(delete_duplicates, A))
    return A[:idx]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sorted_array_remove_dups.py",
                                       'sorted_array_remove_dups.tsv',
                                       delete_duplicates_wrapper))
