from test_framework import generic_test
from binary_tree_node import BinaryTreeNode


def binary_tree_from_preorder_inorder(preorder, inorder):
    if inorder:
        idx = inorder.index(preorder.pop(0))
        root = BinaryTreeNode(inorder[idx])
        root.left = binary_tree_from_preorder_inorder(preorder, inorder[:idx])
        root.right = binary_tree_from_preorder_inorder(preorder, inorder[idx+1:])
        return root


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_from_preorder_inorder.py",
                                       'tree_from_preorder_inorder.tsv',
                                       binary_tree_from_preorder_inorder))
