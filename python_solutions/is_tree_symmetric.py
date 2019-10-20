from test_framework import generic_test


def is_mirror(L, R):
    if not L and not R:
        return True
    elif L and R and L.data == R.data:
        return is_mirror(L.right, R.left) and is_mirror(L.left, R.right)
    return False


def is_symmetric(tree):
    return is_mirror(tree, tree)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_symmetric.py",
                                       'is_tree_symmetric.tsv', is_symmetric))
