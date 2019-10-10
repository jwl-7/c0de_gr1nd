from test_framework import generic_test


def reverse_linked_list(head):
    prev = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev


def is_linked_list_a_palindrome(L):
    slow = fast = L
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    a = L
    b = reverse_linked_list(slow)

    while b:
        if a.data != b.data:
            return False
        a = a.next
        b = b.next
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_list_palindromic.py",
                                       'is_list_palindromic.tsv',
                                       is_linked_list_a_palindrome))
