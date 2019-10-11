import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def list_pivoting(L, x):
    # TODO - you fill in here.
    return None


def linked_to_list(L):
    v = list()
    while L is not None:
        v.append(L.data)
        L = L.next
    return v


@enable_executor_hook
def list_pivoting_wrapper(executor, L, x):
    original = linked_to_list(L)

    L = executor.run(functools.partial(list_pivoting, L, x))

    pivoted = linked_to_list(L)
    mode = -1
    for i in pivoted:
        if mode == -1:
            if i == x:
                mode = 0
            elif i > x:
                mode = 1
        elif mode == 0:
            if i < x:
                raise TestFailure('List is not pivoted')
            elif i > x:
                mode = 1
        else:
            if i <= x:
                raise TestFailure('List is not pivoted')

    if sorted(original) != sorted(pivoted):
        raise TestFailure('Result list contains different values')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("pivot_list.py", 'pivot_list.tsv',
                                       list_pivoting_wrapper))
