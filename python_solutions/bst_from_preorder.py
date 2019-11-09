from test_framework import generic_test
from binary_tree_node import BinaryTreeNode


def rebuild_bst_from_preorder(preorder_sequence):
    if not preorder_sequence:
        return None

    root = BinaryTreeNode(preorder_sequence[0])
    i = 1
    while i < len(preorder_sequence):
        if preorder_sequence[i] < preorder_sequence[0]:
            i += 1
        else:
            break

    root.left = rebuild_bst_from_preorder(preorder_sequence[1:i])
    root.right = rebuild_bst_from_preorder(preorder_sequence[i:])
    return root


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("bst_from_preorder.py",
                                       'bst_from_preorder.tsv',
                                       rebuild_bst_from_preorder))
