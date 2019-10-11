import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def overlapping_no_cycle_lists(L0, L1):
    a = L0
    b = L1
    while a is not b:
        a = a.next if a else L1
        b = b.next if b else L0
    return a


@enable_executor_hook
def overlapping_no_cycle_lists_wrapper(executor, L0, L1, common):
    if common:
        if L0:
            i = L0
            while i.next:
                i = i.next
            i.next = common
        else:
            L0 = common

        if L1:
            i = L1
            while i.next:
                i = i.next
            i.next = common
        else:
            L1 = common

    result = executor.run(
        functools.partial(overlapping_no_cycle_lists, L0, L1))

    if result != common:
        raise TestFailure('Invalid result')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("do_terminated_lists_overlap.py",
                                       'do_terminated_lists_overlap.tsv',
                                       overlapping_no_cycle_lists_wrapper))
