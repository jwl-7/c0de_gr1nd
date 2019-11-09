from test_framework import generic_test


def is_binary_tree_bst(tree, low=float('-inf'), high=float('inf')):
    if not tree:
        return True

    return (
        low <= tree.data <= high and
        is_binary_tree_bst(tree.left, low, tree.data) and
        is_binary_tree_bst(tree.right, tree.data, high)
    )


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_a_bst.py", 'is_tree_a_bst.tsv',
                                       is_binary_tree_bst))
