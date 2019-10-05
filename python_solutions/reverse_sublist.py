from test_framework import generic_test
from list_node import ListNode


def reverse_sublist(L, start, finish):
    dummy = subhead = ListNode()
    dummy.next = L

    for _ in range(1, start):
        subhead = subhead.next
    subtail = subhead.next

    for _ in range(start, finish):
        tmp = subhead.next
        subhead.next = subtail.next
        subtail.next = subtail.next.next
        subhead.next.next = tmp
    return dummy.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("reverse_sublist.py",
                                       "reverse_sublist.tsv", reverse_sublist))
