from test_framework import generic_test


# Assumes L has at least k nodes, deletes the k-th last node in L.
def remove_kth_last(L, k):
    slow = fast = L
    for _ in range(k):
        fast = fast.next
    if not fast:
        return L.next
    while fast.next:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return L


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("delete_kth_last_from_list.py",
                                       'delete_kth_last_from_list.tsv',
                                       remove_kth_last))
