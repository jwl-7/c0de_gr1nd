from test_framework import generic_test


def smallest_nonconstructible_value(A):
    A.sort()
    x = 1
    for num in A:
        if num <= x:
            x += num
        else:
            break
    return x


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("smallest_nonconstructible_value.py",
                                       'smallest_nonconstructible_value.tsv',
                                       smallest_nonconstructible_value))
