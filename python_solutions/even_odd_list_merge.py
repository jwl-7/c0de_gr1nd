from test_framework import generic_test
from list_node import ListNode


def even_odd_merge(L):
    if not L:
        return L
    even = L
    odd = odd_head = even.next
    while odd and odd.next:
        even.next = even.next.next
        odd.next = odd.next.next
        even = even.next
        odd = odd.next
    even.next = odd_head
    return L


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("even_odd_list_merge.py",
                                       'even_odd_list_merge.tsv',
                                       even_odd_merge))
