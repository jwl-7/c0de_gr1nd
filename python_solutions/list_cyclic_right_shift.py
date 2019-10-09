from test_framework import generic_test


def cyclically_right_shift_list(L, k):
    if not L:
        return None

    tail = L
    n = 1
    while tail.next:
        tail = tail.next
        n += 1

    k %= n
    if k == 0:
        return L

    tail.next = L
    for _ in range(n - k):
        tail = tail.next
        
    L = tail.next
    tail.next = None
    return L


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("list_cyclic_right_shift.py",
                                       'list_cyclic_right_shift.tsv',
                                       cyclically_right_shift_list))
