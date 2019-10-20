from test_framework import generic_test


def is_mirror(n1, n2):
    if not n1 and not n2:
        return True
    elif n1 and n2 and n1.data == n2.data:
        return is_mirror(n1.right, n2.left) and is_mirror(n1.left, n2.right)
    return False


def is_symmetric(tree):
    return is_mirror(tree, tree)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_symmetric.py",
                                       'is_tree_symmetric.tsv', is_symmetric))
