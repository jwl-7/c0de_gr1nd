from test_framework import generic_test
from list_node import ListNode


def add_two_numbers(L1, L2):
    dummy = tail = ListNode()
    num = 0
    while L1 or L2 or num:
        if L1:
            num += L1.data
            L1 = L1.next
        if L2:
            num += L2.data
            L2 = L2.next
        tail.next = ListNode(num % 10)
        tail = tail.next
        num //= 10
    return dummy.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("int_as_list_add.py",
                                       'int_as_list_add.tsv', add_two_numbers))
