from test_framework import generic_test


def height(tree):
    if not tree:
        return 0

    left = height(tree.left)
    if left == -1:
        return -1

    right = height(tree.right)
    if right == -1 or abs(left - right) > 1:
        return -1

    return max(left, right) + 1


def is_balanced_binary_tree(tree):
    return height(tree) != -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_balanced.py",
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
