import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast is slow:
            fast = head
            while fast is not slow:
                fast = fast.next
                slow = slow.next
            return fast
    return None


def overlapping_no_cycle_lists(l0, l1):
    a = l0
    b = l1
    while a is not b:
        a = a.next if a else l1
        b = b.next if b else l0
    return a


def overlapping_lists(l0, l1):
    c0 = has_cycle(l0)
    c1 = has_cycle(l1)
    if not c0 and not c1:
        return overlapping_no_cycle_lists(l0, l1)
    if (c0 and not c1) or (not c0 and c1):
        return None

    tmp = c1
    while True:
        tmp = tmp.next
        if tmp is c0 or tmp is c1:
            break
    if tmp is not c0:
        return None

    while l0 is not l1 and l0 is not c0 and l1 is not c1:
        l0 = l0.next
        l1 = l1.next
    return l0 if l0 is l1 else c0


@enable_executor_hook
def overlapping_lists_wrapper(executor, l0, l1, common, cycle0, cycle1):
    if common:
        if not l0:
            l0 = common
        else:
            it = l0
            while it.next:
                it = it.next
            it.next = common

        if not l1:
            l1 = common
        else:
            it = l1
            while it.next:
                it = it.next
            it.next = common

    if cycle0 != -1 and l0:
        last = l0
        while last.next:
            last = last.next
        it = l0
        for _ in range(cycle0):
            if not it:
                raise RuntimeError('Invalid input data')
            it = it.next
        last.next = it

    if cycle1 != -1 and l1:
        last = l1
        while last.next:
            last = last.next
        it = l1
        for _ in range(cycle1):
            if not it:
                raise RuntimeError('Invalid input data')
            it = it.next
        last.next = it

    common_nodes = set()
    it = common
    while it and id(it) not in common_nodes:
        common_nodes.add(id(it))
        it = it.next

    result = executor.run(functools.partial(overlapping_lists, l0, l1))

    if not (id(result) in common_nodes or (not common_nodes and not result)):
        raise TestFailure('Invalid result')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("do_lists_overlap.py",
                                       'do_lists_overlap.tsv',
                                       overlapping_lists_wrapper))
