from test_framework import generic_test
from list_node import ListNode


def even_odd_merge(L):
    even = teven = ListNode()
    odd = todd = ListNode()
    i = 0
    while L:
        if i & 1:
            todd.next = L
            L = L.next
            todd = todd.next
        else:
            teven.next = L
            L = L.next
            teven = teven.next
        i += 1
    todd.next = None
    teven.next = odd.next
    return even.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("even_odd_list_merge.py",
                                       'even_odd_list_merge.tsv',
                                       even_odd_merge))
