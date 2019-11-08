from test_framework import generic_test
from sorted_lists_merge import merge_two_sorted_lists


def stable_sort_list(L):
    if not L or not L.next:
        return L

    prev = None
    slow = fast = L
    while fast and fast.next:
        prev = slow
        fast = fast.next.next
        slow = slow.next
    prev.next = None

    sorted_l1 = stable_sort_list(L)
    sorted_l2 = stable_sort_list(slow)
    return merge_two_sorted_lists(sorted_l1, sorted_l2)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sort_list.py", 'sort_list.tsv',
                                       stable_sort_list))
